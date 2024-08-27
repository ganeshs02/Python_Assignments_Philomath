# FUNCTION ARGUMENTS

'''TYPES
- DEFAULT ARGUMENT
- KEYWORD LENGTH ARGUMENT
- REQUIRED ARGUMENT
- VARIABLE LENGTH ARGUMENT
'''

#1 DEFAULT ARGUMENT HAS SOME DEFAULT VALUE IF DONT PROVIDE -

def average(a=5, b=7): #it will take 5 and 7 as default if not provided
    mean = ((a+b)/2)
    print(f"the average of the value is:  {mean}")


average(5,4)
average(a=2)



#2 keyword argument - in case we dont pass args with a key value syntax then
#it is necessary to pass args in the correct positional order


average(a=9, b=9)


#3 required argument - if we have defined one of variable previoulsy then
# we have to provide remaining variable values



#4 Variable length argument - 

# def average(*numbers):
#it takes the number as a tuple when we add "*" at start
 
# def average(**numbers):
#it takes the number as a dictionary when we add "**" at start 


#tuple example
def average(*numbers): #numbers will be in tuple format (2, 2, 2)
       count = len(numbers)
       total = sum(numbers)
       average = total/count
       print(f"The average is: {average}")


average(2, 2, 2) #output will be 2+2+2/3 = 2.0 



# dictionary format example

def name(**names): #it takes input in dict format (fname = "ganesh"....)
      print(type(names))
      print("hello",names["fname"],names["mname"],names["lname"])

name(fname="ganesh", mname="nilkanth", lname="surle")



# return statement - return statement is used to return the value of
# expression back to calling function

def add_numbers(a, b):
    sum = a + b
    return sum    #after execution of this function it will return the sum value

result = add_numbers(3, 5)
print(result)  # Output: 8
