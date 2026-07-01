local whitelisted = false;
local response = game:HttpGet("https://whitelist.com/whitelist/authentication?key=" .. whitelistKey);
if response == "successfully whitelisted" then
whitelisted = true
end
repeat wait() until whitelisted
print('user has authenticated!');
