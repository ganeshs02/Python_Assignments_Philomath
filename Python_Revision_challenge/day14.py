# finally keyword - after handling all the exceptions it gets executed 
# we can include finally block at the end.
# it gets executed always(used for closing file resources, or ending program etc)
# irrespective of try ad except

try:
    l=[1,2,3,4,5]
    inp = int(input("enter the number you want to print"))
    print(l[inp]) #to print the index in list
except:
    print("you have entered wrong input")
finally: #it always gets excuted at the end 
    print("what ever happens i will get executed!")







#######################################

#Raising cutom errors python - it is used for the program to stop when 
# expected error or condition is occured and which stops program execution.
'''Raise - keyword is used for raising the cutom errors.'''

#1 Example

'''input1 = int(input("enter the integer between 5 to 9: "))
if (input1<5 or input1>9):
    raise ValueError("You have entered wrong int , the value shoul be between 5 to 9")'''


# Raised cutom "value error" for if() condition
###################################

#2 example - program which take input from user and gives error if
#user gives string  as an input except the strig "quit".


'''
while True:
    input2 = input("enter the number between 10 - 20: / or type (quit) to exit:")

    if input2.lower() == "quit":
        print("exiting the program")
        break
    try:
        number = int(input2)
        if 10<= number <=20:
            print("ok")
        else: 
            raise ValueError("you have entered invalid input enter the input between 10 - 20")
    except ValueError as e:
     
        print(f"you have entered the ({e}) input! enter the number between 10-20 or (quit) to exit ")
  
'''