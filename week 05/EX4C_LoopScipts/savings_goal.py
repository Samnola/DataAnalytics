# Savings goal

starting_balance = 5434.00
savings_goal = 15000.00
weekly_savings = 450.00

while starting_balance < savings_goal:
    starting_balance = starting_balance + weekly_savings
    
    if starting_balance > 7500:  #half way point of savings goal 
        print("Almost there! This week my balance is up to", starting_balance)
    
    print("This week my balance increased to", starting_balance)

print("Goal met! My current balance is", starting_balance)
