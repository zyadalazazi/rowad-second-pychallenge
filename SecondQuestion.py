import re
#Reading input from the user
name = input("Please enter your first name:")

#Checking if the name contains digits
while re.search(r'\d', name):
    name = input("Please enter a name that does not contain numbers:")

print("The length of your name is: {0} characters".format(len(name)))