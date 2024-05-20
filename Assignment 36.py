# get a number from user and check if the number is perfect square.

# taking the input from the user
number = int(input("enter any number of your choice:"))
square = 0
# logic to find the perfect square number

if number > 0:
    square = int(number ** 0.5)
    if square * square == number:
        print("the given number is the perfect square")
    else:
        print("the given number is not an perfect square")

else:
    print("enter the positive number first")
