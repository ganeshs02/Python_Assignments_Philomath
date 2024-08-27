#write a program to find factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
#n! = n × (n - 1) factorial formula

print(factorial(10))