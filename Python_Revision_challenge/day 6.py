# Match case statement 
#it checks the variable with the predefined test cases !
#if it didnt match it returns the default case

#example - 

x = (input("enter any number of you choice:"))

if type(x) == int: #case1
    print("The input is integer")
elif type(x) == str:  #case2
    print("The input is the string")
elif type(x) == float:  #case3
    print("The input you provided a float ")
else:                    #default case
    print("I think You have entered nothing!")
