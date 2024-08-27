#You are given two positive integers
# 1. Height of ladder and 2. Max number of steps  you can take at a time to
# reach the top. Write a program to list all possible ways in which one
# can reach to the top of the ladder.

height = int(input("enter the height of the ladder:"))

steps = int(input("enter the number of steps of the ladder:"))

def laddercount(height,steps):
    if height == 0 or height == 1:
        return 1
    else:
        return(height//steps) + (1 if height % steps != 0 else 0)


print(laddercount(height,steps))


