
#Given 21 Matchsticks and 2 users, A and B (computer and user respectively). Users can pick matchsticks not more than four at a time. The one who is forced to pick the last matchstick loses. 
import random

new_game = True
while True:
    game_choice = 'y'
    if new_game:
        game_choice = input("Press 'y' to play or 'q' to quit the game: ").lower()
    else:
        game_choice = input("Press 'y' to play again or 'q' to quit the game: ").lower()
    if game_choice == 'q':
        break
    new_game = False

    # Game starts here
    matchsticks = 21
    first_to_play = random.getrandbits(1)
    last_user = first_to_play
    print("Game starts, matchsticks =", matchsticks)
    while matchsticks > 0:
        if first_to_play:
            match_remove = int(input("Pick matchsticks (at most 4): "))
            if match_remove < 1 or match_remove > 4:
                print("You chose an invalid number of matchsticks. You lose!")
                break
            elif match_remove > matchsticks:
                print("You are the last to choose. You lose!")
                break
            else:
                matchsticks -= match_remove
                if matchsticks == 0:
                    print("You lose!")
                    break
                last_user = 1
        else:
            # Simulating computer's turn by picking 1 matchstick
            matchsticks -= 1
            print("Computer picks 1 matchstick.")
            if matchsticks == 0:
                print("Computer loses!")
                break
            last_user = 0
