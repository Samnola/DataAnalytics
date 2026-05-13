# Exercise 2B
import random
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# 4A)
product_of_the_day = random.choice(products)
print("Product of the Day:", product_of_the_day)

# Three products need to be selected. Same product can't appear more than once.
# 4B)
survey_products = random.sample(products, 3)
print("Survey Products:", survey_products)

# 4C)
random.shuffle(products)
print("All Products:", products)

#4D)

daily_transactions = random.randint(50, 300)
print("Daily Transactions:", daily_transactions)