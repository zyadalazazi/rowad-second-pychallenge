import re

#Reading inputs from the user: first name and surname
f_name, s_name = input("Please enter your first name:"), input("Please enter your surname:")
full_name = f_name+" "+s_name

#Checking if none of the names contains digits
while re.search(r'\d', full_name):
    print("Please enter names that do not contain numbers!")
    f_name, s_name = input("Please enter your first name:"), input("Please enter your surname:")
    full_name = f_name + " " + s_name

#Printing the output: full name and the its length excluding any spaces
print("Your full name is: {0} {1}, and it has a length of: {2}".format(f_name, s_name, len((f_name+s_name).strip(" "))))