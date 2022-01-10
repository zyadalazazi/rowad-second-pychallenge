#Reading the age from the user
user_age = input("Please enter your age:")

#Validating that the age is appropriate (not a string and above 0)
fl = False
while(fl == False):
    if (user_age.isalpha()):
        user_age = input("Please enter a valid age that is not alphabetic characters:")
    elif (int(user_age)<=0):
        user_age = input("Please enter a valid age that is greater than 0:")
    else:
        fl = True

#Printing the output depending on the proper age
if (int(user_age)>=18):
    print("\nYou can vote.")
elif(int(user_age)==17):
    print("\nYou can learn to dive.")
elif(int(user_age)==16):
    print("\nYou can buy a lottery ticket.")
else:
    print("\nYou can go trick or treating")