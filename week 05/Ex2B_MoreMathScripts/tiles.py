# You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You
# can only buy full boxes, not a partial box.

import math

#get length & width
length = float(input("Enter room length:"))
width = float(input("enter room width:"))

area = length * width

#calculate boxes 
boxes = math.ceil(area/12)
print(f"You need {boxes} boxes of tile.") 

# {} tells python to grab variable inside box 