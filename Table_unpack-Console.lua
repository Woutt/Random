rconsoleclear()

getgenv().serializeTable = function(val, key, inline, level)
    inline = inline or false
    level = level or 0
    local tab = string.rep("    ", level)   -- vroeger 'indent'
    if key then tab = tab .. key .. " = " end

    if type(val) == "table" then
        local result = tab .. "{" .. (not inline and "\n" or "")
        for k,v in pairs(val) do
            result = result .. serializeTable(v, k, inline, level + 1) .. "," .. (not inline and "\n" or "")
        end
        result = result .. string.rep("    ", level) .. "}"
        rconsoleprint(result)
        return result
    elseif type(val) == "string" then
        val = string.format("%q", val)
    elseif type(val) == "boolean" then
        val = val and "true" or "false"
    else
        val = tostring(val)
    end

    local result = tab .. val
    rconsoleprint(result)
    return result
end
