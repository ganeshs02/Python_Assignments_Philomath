# Excercise Snake water gun game in python


import random #library to print the random integers

# function to check conditions for losing  or winning
def check(comp, user):
    if comp == user: #return 0 if both chooses are same
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1
    return 1 # if wins then return 1 

################################
#input form user and computer 

user = int(input("choose 0 for snake , 1 for water and 2 for gun:\n"))
comp = random.randint(0,2)
#####################################

#to check the score after input into the if else conditions 
score = check(comp, user)

#########################################
#to print coices made by computer and user

print(f"you:{user}")
print(f"computer:{comp}")

#########################################################
# conditions to print result from the condtions output

if (score == 0):
    print("Its a draw!")
elif (score == -1):
    print("you lose!")

else:
    print(" congratulations You won !!!")

###################################################################################################

'''Random library - used to generate random outputs'''
import random
'''
print(random.randint(0,100)) #chooses random numbers from 0-100
print(random.randint(0,100)) 
print(random.randint(0,100)) 
print(random.randint(0,100)) 
print(random.randint(0,100)) 
'''
