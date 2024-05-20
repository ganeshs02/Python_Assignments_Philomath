#Get a number from user, write a program to calculate factorial of the number using for loop and while loop

number = int(input("enter the number to find the factorial: "))


def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
    
print("the number of the factorial is " , factorial(number))