# Exceptions basics

try:
    # Trying to turn text into an integer 
    number = int("hello")

except ValueError: # right type, wrong value 
    print("ValueError: You entered invalid data.")

else:
    print(number)

finally:
    print("Let;s try another one... \n")

# NAME ERROR 

try:
    #variable does not exist
    print(banana)

except NameError:
    print("No errors found.")

finally: 
    print("Let's try another one... \n")

# TYPE ERROR
# Wrong data types together 
try:

    # Cannot add string and integer 
    result = "5" + 5

except TypeError:
    print("TypeError: Cannot combine string and integer. ")

else:
    print(result)

finally:
    print("Let's try another one... \n")

# SYNTAX ERROR 
# Python grammer mistake 
# Syntax error crashes before running
# so we simulate it using eval()

try:

    eval("if True print('hello')")

except SyntaxError:
    print("SyntaxError: Invalid syntax detected.") 

else:

    print("Code ran successfull.")

finally: 
    print("Let's try another one... /n")