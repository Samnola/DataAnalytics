# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?

import math
tourists = int(input("Number of tourists"))
vans_needed = math.ceil(tourists / 15) #using ceiling since ppl cant partially exist in one van 

print(f"Number of vans needed: {vans_needed}")

total_van_rental = 250 * vans_needed
cost_per_person = math.ceil(total_van_rental / tourists)

print(f"Total cost per person: {cost_per_person}")

# a) How much money did your script say you had to charge per person?
#$20 per person

#b) If you multiply that out, how much did you collect? 
# $760

#c) How much were the vans?
# $750

#d) Why do you have leftover money?
# I had left over because I used the ceiling round function since we cant put 
# parts of a tourists in a van and need to round up. 