#day 2
# if -else -elif statements #


#excercise 2

'''inp1 = int(input("enter your age:"))
limit = 18


if  inp1 < 7 or inp1>100:
    print("You have eneterd invalid age")
elif inp1 == limit:
    print("you are eligible ! give the test to drive")
elif inp1 < limit :
    print("You are not eligible to drive")
elif inp1 > limit :
    print("congratulaitons ! you are eligible to drive")
'''

    ###################

   # excercise 2
'''
var1 = 52
var2 = 50
var3 = int(input("enter variable 3:"))


if var3 > var1 and var2:
    print("The third vairable is greater")

elif var1 > var2:
    print("var1 is greater than var2")

else:
    print("var2 is greater")'''
#########
'''
list1 = list(input("enter any list:"))

# in keyword

if 4 in list1:
    print("the number 4 is present in the list")
else:
    print("the number is not present in the list")'''


#excercise 3 #faulty calculator
 
#45*3 = 555 , #56+9 = 77, #56/6 = 4


first = int(input("enter the first number:"))
second = int(input("enter the second number:"))
operators = input(print("select on of the operator from following : *, +, /, - :"))


if first == 45 and second == 3 and operators == "*":
    print("555")
elif first == 56 and second == 9 and operators == "+":
    print("77")
elif first == 56 and second == 6 and operators == "/":
    print("4")

#original calculator
elif operators == "+":
    print((first)+(second))

elif operators == "-":
    print((first) - (second))

elif operators == "*":
    print((first) * (second))

elif operators == "/":
    print((first) / (second))

else:
    print("you have entered invalid input")