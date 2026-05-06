# Restaurant tip calculation
print()

bill = 120
tip_percentage = 0.20
tip_amount = bill *tip_percentage
print(tip_amount)

print("The tip on a $" + str(bill) + " restaurant bill is $" + str(tip_amount))
print()

# Calculations continued 
print()
bill= 337
tip_percentage = 0.25
print(tip_percentage)
tip_amount = bill *tip_percentage
print("The tip on a $" + str(bill) +" restaurant bill is $" +str(tip_amount))

print()

# more calculations

bill = 726.34
tip_percentage = .30

tip_amount = bill * .30

print("The tip on a $ " + str(bill) + "restaurant bill is $ " + str(tip_amount))
#tip amount was 217.90200000000002
# if I want the total to be rounded two places -------> tip_amount = round(bill *.30, 2)

# Tip calculations with rounding 

bill = 97.58
tip_percentage = bill * tip_percentage
tip_amount = round(bill * .20,2 )

print("The tip on a $ " + str(bill) + " restaurant bill is $" + str(tip_amount))