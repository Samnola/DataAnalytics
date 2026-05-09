# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

#print(int(a)) error message
#int cant contain decimals hence error msg.
print(int(float(a)))

print(int(b)) #works because its already integer

# print(int(c)) # ValueError
#print(int(float(c))) # ValueError
# cannot convert because string contains text and numbers.

#print(int(d))
#print(float(d))
#will not convert text and numbers in string. 

print(int(c[0:3])) 
#if the left side of colon is empty = start from beginning
#if right side of colon is empty go all the way to the end

#strip removed leading & trailing spaces

print(a.strip())

print(d.strip())
# does not remove spaces in the middle. only cleans outside white space