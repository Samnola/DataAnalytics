# Area of rectangle
print()
side_a= 27
print("Side A is", side_a)
side_b=2
print("Side B is", side_b)
area_of_rectangle= side_a * side_b
print("Area of rectangle is " + str(area_of_rectangle))

# using (input)

side_a = int(input("Enter side A: "))
print("Side A is " + str(side_a))
# A potential pitfall to doing this would be the user tpying letters when Im expecting a number. 
# user could also potentially leave blank or use unexpected characters which would display an error. 
