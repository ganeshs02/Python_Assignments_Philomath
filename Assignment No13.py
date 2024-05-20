#Ask user to enter number check if number is 0 or less than 0 or greater than 0

number = int(input("enter the numbber:"))

if number < 0:
    print("the number is less than 0")
elif number == 0:
    print("the number is equals to 0")
elif number > 0:
    print("the number is greater than 0")