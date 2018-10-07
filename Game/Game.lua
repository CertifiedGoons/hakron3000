
deck_guid = '6055c0'



function onload()
deck = getObjectFromGUID(deck_guid)

    
takeParams = {}
takeParams.position = {x=5, y=0, z=5}
takeParams.flip = true
takeParams.index = 1

for i=1, 40 do
deck.takeObject(takeParams)
end

end


