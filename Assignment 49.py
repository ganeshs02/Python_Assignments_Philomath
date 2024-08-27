#write a program to compute factorial of a number using function

number = int(input("enter any number of your choice:"))
count = 0
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)


result = factorial(number)
print(f"the factorial of the given {number}, is {result}")