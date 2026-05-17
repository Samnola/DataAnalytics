# OPEN AND WRITE FILES LAB

# open () creates or opens a file 
# "a" means Append 
# append adds info to a file
# if file does not exist python creates it 

f = open("about_me.txt", "a")

# close () closes the files after using it 
# this is important so python saves everything properly 

f.close()

# w means WRITE 
# write mode replaces old contents with new 

f = open("a;bout_me.txt", "w")

# write () adds text into file 
# \n line breaks 

f.write("Name:Alondra Martinez \n")
f.write("Place of birth: Mexico City \n")
f.write("Pets growing up: Dogs \n")
f.write("If I could travel anywhere for one week: Japan \n")
f.write("If I could live anywhere for a year: Portugal \n")

f.close()

# REOPEN FILE IN APPEND MODE 

f = open("about_me.txt", "a")

f.write("\n")

f.write("Perfect night out : ")
f.write("Dinner at a rooftop restaurant ")
f.write("followed by exploring a city at night. \n")

f.close()

print("about_me.txt updated succesfully! ")