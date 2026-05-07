# Rule of 72
print()
current_savings = 125600
interest_rate = 7
years = 72 / interest_rate
doubled_balance = current_savings * 2
print("Your current savings is $" + format(current_savings, ".2f"))
print("At a " + format(interest_rate / 100, ".0%") + " interest rate, your savings account will be worth $ " + format(doubled_balance, ".2f") + " in " + format(years, ".1f") + " years ") 


