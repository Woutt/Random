local oldHttpGet; do
    oldHttpGet = hookfunction(game.HttpGet, function(self, url, ...)
        if typeof(url) == "string" then
            if string.find(url, "https://whitelist.com/whitelist/authentication") then
                return "successfully whitelisted"
            end
        end
        return oldHttpGet(self, url, ...)
    end)
end
