# OPEN AND READ FILES LAB
# "r" means read

f = open("about_me.txt", "r")

# READ ENTIRE FILE 

# print(f.read())

# STEP 15A 
# Store first 50 characters 

first_variable = f.read(50)

# STEP 15B

second_variable = []

for i in range(1, 5):
    second_variable.append(f.readline())

# STEP 15 C

third_variable = f.readlines(100)

# STEP 16 OUTPUT

print("First 50 characters:")
print(first_variable)

print()

print("Next four lines, as list by line:")
print(second_variable)

print()

print("Next 100 characters, as list by line:")
print(third_variable)

f.close()