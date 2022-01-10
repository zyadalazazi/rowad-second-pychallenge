#Reading input from the user
favorite_color = input("Please enter your favorite color:")

#Checking that the input is not a number
while favorite_color.isnumeric():
    favorite_color = input("Please enter a valid color not a number:")

#Printing the appropriate output
if(favorite_color.lower() == "blue"):
    print("I like blue too")
else:
    print("I don’t like {0}, I prefer blue".format(favorite_color))
