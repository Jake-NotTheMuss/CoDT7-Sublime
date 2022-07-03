-- SYNTAX TEST "Packages/CoDT7 Formats/LUI.sublime-syntax"

LUI = {}
-- <- source.lua.lui

Engine.Exec("disconnect")
--     ^ meta.engine-function.lua.lui

Enum.LobbyType.LOBBY_TYPE_PRIVATE = 0
--   ^ meta.lui-enum-group
--             ^ meta.lui-enum-id
