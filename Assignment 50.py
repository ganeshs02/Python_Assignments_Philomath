#Write a program to get fibonacci number of given number


number = int(input("enter the number of your choice:"))

def fibonacci(number):
    if (number == 0 or number == 1):
        return number
    else:
        return (fibonacci(number-1)) + (fibonacci(number-2))


print(fibonacci(number))
