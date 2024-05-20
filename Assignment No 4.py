'''
"Write a programe to define a variable a=10 and b=20 and swap values of the variables. 
Output should display:
initial value of a is: <actual vaule of a> and initial value of b is: <actual value of b>
value of a after swap is: <actual vaule of b> and value of b after swap is: <actual value of a>"
'''

a = 10 
b =20

print(a)
print(b)

a,b = b,a

print("value of a:",a)

print("value of b:",b)


###############################################################################################################

#Quiz -  make calcuator which take input of 2 numbers from user and adds two numbers


num1 = int(input("enter 1st number :"))
num2 = int(input("enter 2nd number :"))
num3: int = num1+num2

print("The total of the two numbers is :", num3)


