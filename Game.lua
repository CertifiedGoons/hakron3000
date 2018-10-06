
function onload()
    spawnObject({["type"] = "Deck"})
    findInRadiusBy({0,0,0}, 100, function(o) return o.tag=="Card" end, true)
    cards = findInRadiusBy()
    for k, v in pairs(arr) do
        print(k)
end

function findInRadiusBy(pos, radius, func, debug)
    local radius = (radius or 1)
    local objList = Physics.cast({
        origin=pos, direction={0,1,0}, type=2, size={radius,radius,radius},
        max_distance=0, debug=(debug or false)
    })

    local refinedList = {}
    for _, obj in ipairs(objList) do
        if func == nil then
            table.insert(refinedList, obj.hit_object)
        else
            if func(obj.hit_object) then
                table.insert(refinedList, obj.hit_object)
            end
        end
    end

    return refinedList
end

