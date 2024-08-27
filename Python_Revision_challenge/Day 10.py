#  f-strings  #to use the variables inthe string

#example 
'''username = input("enter yourname:")
age = input("enter your age:")

print(f"hello mr {username} , your age is{age}.") #fstring

'''
##########

#Docstring in python
# these are used to right above the functon to document your functions

#example 
''
def square(n):
    '''takes in a number n return the  #working of the function
    square of the n'''
    print(n**2)

#square(5)
#print(square.__doc__) ''#it prints the documnetation written in the function .S


################################

#Recursion = calling function in the same function.
#when function calls itself it is called as "recursive function".

#example no.1 - To find factorial of the any number.
# f(7) = 7*6*5*4*3*2*1

#The logic for printig factorial is f(n) = n*f(n-1)

'''def factorial (n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n*factorial (n-1))
    

print(factorial(5))

'''

#example no.2 - printing of the fibonnaci series of the numbers
'''formula - f(0) = 0
           f(0) = 0
           f(1) = 1
           f(2) = f(1) + f(0)
           f(n) = f(n-1) + f(n-2)'''

a = int(input("enter the number of character in series"))

def fibonnaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fibonnaci(n-1))+(fibonnaci(n-2))
for i in range (a):
    print(fibonnaci(i))
