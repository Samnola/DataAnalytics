# Define known values
print()
food_cost = 79.25
tax = 6.54
tip = 12.00

#Calculate the unknown
print ()
total_due = food_cost + tax + tip

#Display the results
#print("The total due is " + str(total_due))
print () 
# str() converts values like numbers or other data into strings so they can be shown 

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
print("Tip is " + str(tip))
print("Total due is " + str(total_due))
# print ("Tip is" + str(tip))
print("Tip is" + format(tip, ".2f"))