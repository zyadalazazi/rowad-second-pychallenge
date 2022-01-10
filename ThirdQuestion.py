#Reading the input from the user
user_word = input("Please enter any word:")

#Making sure that the user does not enter numbers for a word
while(user_word.isnumeric()):
    user_word = input("The word you entered is a number, please enter a word composed"
                      "of alphabetic characters:")

#Printing the output
print("The word you entered is: {}".format(user_word.upper()))