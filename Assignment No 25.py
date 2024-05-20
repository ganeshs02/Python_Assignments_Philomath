#Given 21 Matchsticks and 2 users, A and B (computer and user respectively). Users can pick matchsticks not more than four at a time. The one who is forced to pick the last matchstick loses.Â 


import random

def computer_move(matchsticks_left):
    if matchsticks_left <= 4:
        return matchsticks_left
    else:
        return ramdom.randint(1, 4)


def user_move(matchsticks_left):
    while True:
        user_input = int(input("your turn .Pick 1 to 4 matchsticks:"))
        if 1 <= user_input <= 4 and user_input <= matchsticks_left:
            return user_input
        else:
            ("print you have entered the invalid input")


def play_game():
    matchsticks_left = 21

    while matchsticks_left > 0:
        #computer move
        computer_pick = computer_move(matchsticks_left)
        print("computer picks", computer_pick, "matchstick(s).")
        matchsticks_left -= computer_pick
        print("matchsticks left:",matchsticks_left )



def play_game():
    matchsticks_left = 21

    while matchsticks_left > 0:
        # Computer's move
        computer_pick = computer_move(matchsticks_left)
        print("Computer picks", computer_pick, "matchstick(s).")
        matchsticks_left -= computer_pick
        print("Matchsticks left:", matchsticks_left)

        # Check if the game is over
        if matchsticks_left <= 0:
            print("You win! The computer picked the last matchstick.")
            break

        # User's move
        user_pick = user_move(matchsticks_left)
        matchsticks_left -= user_pick
        print("Matchsticks left:", matchsticks_left)

        # Check if the game is over
        if matchsticks_left <= 0:
            print("Computer wins! You picked the last matchstick.")
            break


play_game()
        
        