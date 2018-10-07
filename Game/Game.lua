
deck_guid = '6055c0'



function onload()
deck = getObjectFromGUID(deck_guid)

    
takeParams = {}
takeParams.position = {x=5, y=0, z=5}
takeParams.index = 1
takeParams.flip

deck.takeObject(takeParams)

end

