# Min Max
a = 12
b = 25
c = 3

# Determing smallest numhber
if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else: 
    smallest = c

# Determing largest number 
if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c

print("Smallest number:", smallest)
print("Largest number:", largest)