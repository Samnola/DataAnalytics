# more loops

foods = ["tacos","sopes","tamales","baleadas","picanha"]

# For each food in my foods list, also keep track of the number starting at 1
for index, food in enumerate(foods, start=1):
    if index == 1:
        print(index, food, " Top pick!")

    
        