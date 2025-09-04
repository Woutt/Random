-- this was for looking trough all game files and filtering in roblox 
-- (If the executor has getfenv as a stable function, you can use it... otherwise it will crash hehehe)

--//settings
local check_path_last_name = "MainClient" --if you want every funciton just set this to nil
local Get_Full_Name = true --bool
local no_dubble_functions = true --bool
local file_name = "functions.txt" --string





local file_bool,tbl = false, {}
local function file(a,b)
    if file_bool == false then
        writefile(a, "")
        file_bool = true
    end
    if b then
        appendfile(a, b.."\n")
    end
end
for i,v in pairs(getgc()) do
    if type(v) == "function" and islclosure(v) and not is_synapse_function(v) then
        if check_path_last_name ~= nil then
            if tostring(check_path_last_name) == tostring(getfenv(v).script) then
                if no_dubble_functions then
                    if getinfo(v).name and not table.find(tbl,getinfo(v).name) then
                        table.insert(tbl,getinfo(v).name)
                        if Get_Full_Name then
                            file(file_name,getinfo(v).name.." | "..tostring(getfenv(v).script:GetFullName()))
                        else
                            file(file_name,getinfo(v).name.." | "..tostring(getfenv(v).script))
                        end
                    end
                else
                    if Get_Full_Name then
                        file(file_name,getinfo(v).name.." | "..tostring(getfenv(v).script:GetFullName()))
                    else
                        file(file_name,getinfo(v).name.." | "..tostring(getfenv(v).script))
                    end
                end
            end
        else
            if no_dubble_functions then
                if getinfo(v).name and not table.find(tbl,getinfo(v).name) then
                    table.insert(tbl,getinfo(v).name)
                    if Get_Full_Name then
                        file(file_name,getinfo(v).name.." | "..tostring(getfenv(v).script:GetFullName()))
                    else
                        file(file_name,getinfo(v).name.." | "..tostring(getfenv(v).script))
                    end
                end
            else
                if Get_Full_Name then
                    file(file_name,getinfo(v).name.." | "..tostring(getfenv(v).script:GetFullName()))
                else
                    file(file_name,getinfo(v).name.." | "..tostring(getfenv(v).script))
                end
            end
        end
    end
end

