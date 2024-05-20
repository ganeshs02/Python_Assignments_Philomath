#Ask user to pick any number between 0 and 100 and implement a guessing game program to identify number picked up by user.
# (use while loop)

import random

message1 = "welcome to the number guessing name"
message2 = "follow the instructions to play the game!!"
entered_number = int(input("select any number between 1 to 100"))

#initialization of the variables
guesses = 0
min_number = 0
max_number = 100
guessed_number = None

#creation of the loop for the game

while guessed_number != entered_number:
    guessed_number = random.randint(min_number,max_number)

#incrementing the guesses

guesses+=1

print("The number guessed by computer is :", guessed_number)

#condition if the number is smaller or larger
if guessed_number < entered_number:
    print("too low!")
    min_number = guessed_number+1

elif guessed_number > entered_number:
    print("too high!")
    max_number = guessed_number-1

    #final result declaration

print(f"computer finally guessed your number:{entered_number}number in {guesses}!")