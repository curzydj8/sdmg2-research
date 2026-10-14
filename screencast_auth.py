#!/usr/bin/env python3
"""触发 ScreenCast 授权框：走完整 portal 流程，用户在弹窗点允许并记住"""
import sys, random

def main():
    try:
        import gi
        gi.require_version('Gio', '2.0')
        from gi.repository import Gio, GLib
    except Exception as e:
        print(f"ERROR: gi 不可用: {e}")
        return 1

    bus = Gio.bus_get_sync(Gio.BusType.SESSION, None)

    def await_response(req_path, timeout_s):
        """等待 portal Request 的 Response 信号，返回 (response_code, results_dict)"""
        out = {}
        loop = GLib.MainLoop()
        proxy = Gio.DBusProxy.new_sync(bus, Gio.DBusProxyFlags.NONE, None,
            'org.freedesktop.portal.Desktop', req_path,
            'org.freedesktop.portal.Request', None)
        def on_signal(p, sender, path, iface, name, params):
            if name == 'Response':
                out['code'] = params[0]
                out['results'] = dict(params[1])
                loop.quit()
        proxy.connect('g-signal', on_signal)
        GLib.timeout_add_seconds(timeout_s, loop.quit)
        loop.run()
        return out.get('code'), out.get('results', {})

    portal = Gio.DBusProxy.new_sync(bus, Gio.DBusProxyFlags.NONE, None,
        'org.freedesktop.portal.Desktop', '/org/freedesktop/portal/desktop',
        'org.freedesktop.portal.ScreenCast', None)

    # 1. CreateSession
    print("步骤 1/3: CreateSession...", flush=True)
    stoken = f"session{random.randint(1000,9999)}"
    req = portal.CreateSession('(a{sv})',
        {'session_handle_token': GLib.Variant('s', stoken)})
    code, results = await_response(req, 30)
    if code != 0 or 'session_handle' not in results:
        print(f"ERROR: CreateSession 失败 (code={code})")
        return 1
    shandle = results['session_handle']
    print(f"  session: {shandle}", flush=True)

    # 2. SelectSources
    print("步骤 2/3: SelectSources...", flush=True)
    sproxy = Gio.DBusProxy.new_sync(bus, Gio.DBusProxyFlags.NONE, None,
        'org.freedesktop.portal.Desktop', shandle,
        'org.freedesktop.portal.ScreenCast', None)
    req = sproxy.SelectSources('(oa{sv})', shandle,
        {'types': GLib.Variant('u', 1 | 2),
         'multiple': GLib.Variant('b', True),
         'handle_token': GLib.Variant('s', f"sel{random.randint(1000,9999)}")})
    code, _ = await_response(req, 60)
    if code != 0:
        print(f"ERROR: SelectSources 失败 (code={code})，请检查是否在弹窗点了允许")
        return 1
    print("  OK", flush=True)

    # 3. Start —— 弹出系统授权框
    print("步骤 3/3: Start —— 授权框应该弹出来了，请点允许并勾选记住...", flush=True)
    req = sproxy.Start('(osa{sv})', shandle, '',
        {'handle_token': GLib.Variant('s', f"start{random.randint(1000,9999)}")})
    code, results = await_response(req, 120)
    if code == 0:
        print(f"SUCCESS: 授权成功！streams: {results.get('streams')}")
        return 0
    print(f"ERROR: Start 失败 (code={code})")
    return 1

if __name__ == '__main__':
    sys.exit(main())
