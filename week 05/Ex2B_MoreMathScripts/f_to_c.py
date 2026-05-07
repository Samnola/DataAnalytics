# How do you convert a temperature from Fahrenheit to Celsius?


fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# use float because temperatures can be displayed with decimals
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is equal to {celsius:}°C")
