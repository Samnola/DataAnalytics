print ('Hello world!')


message= 'Hello world!'
print(message)
# Hello world is displaying twice because it runs everything at once and ther is no way to run a single query individually. 


# Displaying dollars and cents

dollars = 3
cents = 0.50
print(dollars+cents)
# The result showed 3.5 instead of 3.50 because python removed zeros in decimal numbers. 
cents = cents + .25
print(dollars+cents)

d_str = "3 dollars"
c_str = "50 cents"
print(d_str + " " + c_str)