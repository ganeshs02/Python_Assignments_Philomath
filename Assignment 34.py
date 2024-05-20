# Get a number from user and check if number is twin prime number

# defining the function

def prime(number):
    if number == 1 or number == 2:
        return True
    for i in range(2, int(number * 0.5 + 1)):
        if number % i == 0:
            return False

    return True


num = int(input("enter the number"))

if prime(num):
    if prime(num + 2):
        print("The number is the twin prime number!")
    else:
        print("This is not a twin prime number!")

else:
    print("The number is not a prime number!!")
