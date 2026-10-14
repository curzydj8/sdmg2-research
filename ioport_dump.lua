-- ioport_dump.lua
-- MAME Lua script: dump runtime I/O port values AND the actual key/joy
-- sequences bound to each input field (incl. Bet = IPT_BUTTON2 "押注").
-- Usage on an INDEPENDENT test instance only (never the live Wayland PID):
--   mame sdmg2754ca -script ioport_dump.lua
-- (-script executes the file after machine boot; no debugger, no recompile.)
-- Output: /tmp/ioport_dump.txt
--
-- API basis: docs.mamedev.org/luascript/ref-input.html
--   manager.machine.ioport.ports[tag]  -> port objects keyed by absolute tag
--   port:read()                        -> current 32-bit input value
--   port.fields[name]                  -> field objects keyed by display name
--   field.mask / field.defvalue / field.live / field.type / field.player
--   ioport:input_type_to_token(type, player) -> token like "DIPSWITCH"
--   field.seq / field.default_seq      -> Sequence objects (current/default
--                                          key+joy bindings); tostring best-effort
--   ioport:type_seq(type, player, seqtype) -> manager-level default sequence
--                                          (seqtype 0 = standard)
--
-- STATUS (2026-10-14): prepared but UNTESTED. This MAME 0.285 build's Lua
-- support is unconfirmed: INPUT-TEST-REPORT.md (00:45 UTC) found no script
-- options in `mame -help`, but that check returned empty output (binary may
-- not have run properly). If the build lacks Lua, `mame -script ...` will
-- fail immediately with an error -- that alone is a useful, cheap answer.

local OUTFILE = "/tmp/ioport_dump.txt"

local out, err = io.open(OUTFILE, "w")
if not out then
  print("ioport_dump: cannot open " .. OUTFILE .. ": " .. tostring(err))
  return
end

local function w(s) out:write(s .. "\n") end

local function safe_seq(label, fn)
  local ok, seq = pcall(fn)
  if not ok then
    return label .. "=ERR:" .. tostring(seq)
  end
  local ok2, s = pcall(tostring, seq)
  if not ok2 then
    return label .. "=TOSTRING-ERR:" .. tostring(s)
  end
  return label .. "=" .. tostring(s)
end

local iop = manager.machine.ioport
w("== ioport dump ==")
w("system: " .. manager.machine.system.name)

for tag, port in pairs(iop.ports) do
  local ok, val = pcall(function() return port:read() end)
  w(string.format("PORT tag=%s read=%s", tostring(tag),
    ok and string.format("0x%08X", val) or ("ERR:" .. tostring(val))))
  local ok2, fields = pcall(function() return port.fields end)
  if ok2 and fields then
    for fname, field in pairs(fields) do
      local tok = iop:input_type_to_token(field.type, field.player)
      w(string.format("  FIELD name=%q token=%s mask=0x%X defvalue=%s live=%s",
        tostring(fname), tostring(tok), field.mask,
        tostring(field.defvalue), tostring(field.live)))
      -- The lines below answer "which KEY is bound to this input":
      w("    " .. safe_seq("seq", function() return field.seq end))
      w("    " .. safe_seq("default_seq", function() return field.default_seq end))
      w("    " .. safe_seq("type_seq_std",
        function() return iop:type_seq(field.type, field.player, 0) end))
    end
  end
end

w("== end ==")
out:close()
print("ioport_dump: wrote " .. OUTFILE)
