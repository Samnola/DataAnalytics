# Candy store

candies = ("Gummies", "Lollipop", "Taffy")
flavors = ("lemon", "Raspbery", "Watermelon")

candy_options = {
    candies[0] + " " + flavors[0],
    candies[1] + " " + flavors[1],
    candies[2] + " " + flavors[2]
}

print("Today's candy options include:")
print(candy_options)
# as I print output multiple times I notice 
# sets dont keep items in fixed order