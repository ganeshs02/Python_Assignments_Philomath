#ask user to pick any number between 0 and 100 and implement a guessing game program to identify number picked up by user. (use while loop)
import random 

#welcome messages for the game
message1 = print("Welcome to the number guessing game!!!")
message2 = print("Please select any number between 0 to 100 ")
#took user input for the guessing
entered_number = int(input("Select your number"))

#initialized the variables
guesses = 0
min_number = 0
max_number = 100
guessed_number = None

#while loop for the for guessing game
while guessed_number != entered_number:
    #to generate the ramdom guesses
    guessed_number = random.randint(min_number, max_number)


    #increment the number guesses
    guesses += 1

#print the guesses
    print("computers guesses:", guessed_number)

#adjust the range for the next guess
    if guessed_number < entered_number:
        print("Too low !")
        min_number = guessed_number + 1
    elif guessed_number > entered_number:
        print("Too high!")
        max_number = guessed_number -1

#print the number for the gussed number
print(f"Computer gussed your number ({entered_number}) in {guesses} gusses!")







