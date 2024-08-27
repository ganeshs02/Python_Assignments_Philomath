#try and except handling
#try and except is used to hadle error except instead of throwing the error.

#example -

'''
try:
    result = 10/0   #risky code which may throw error
except Exception as e:
    print(f"an error occured: {e}") # it wil execute if error occur
finally:
    print("this line is important") #this block wil always execute.
'''


##########
#kaun banega crorepati game


########
print("Namaskar doston mai amitabh bacchan aapka swagat karta hoon , Kaun banega crorepati ki pehle episode main!")
name = input("Kya main aapka naam jaan sakta hoon?:")
print(f"{name} ji aapka swagat hai , chaliye khel shuru karte hain!")
########################################################################
q1 = ["what is the capital of the india?",["1.Maharshatra","2.kolkata","3.bihar","4.delhi"]]
q2 = ["which of the following is independance year of india?",["1. 1777","2. 1999", "3.1947", "4.1956"]]
q3 = ["which of the the follwing is the national bird of india?",["1. sparrow","2. parrot", '3.peacock', "4.raven"]]
q4 = ["which of the following is the captain of indian cricket team in 2011?"],["1. yurvraj singh", "2. ms.dhoni", "3.gautam gambhir", "4.sachin tendulkar"]
q5 = ["which of the followig is the name of shivaji maharaj's talwar"],["1. jagdamb", "2.neel", "3.tejas", "4.vikram"]
########################################################
i = 0
print(q1[0])
print(q1[1])
ans = input("enter your answer:")
if ans == "4":
    print("correct answer😁!")
    print("you have won 10k")
    i = i+10
else:
    print("worng answer!")
    print("better luck next time😯")
    exit() #to break code execution 
########################################################
print(q2[0])
print(q2[1])
ans = input("enter your answer:")
if ans == "3":
    print("correct answer😁!")
    print("you have won 20K")
    i = i+10
else:
    print("wrong answer!")
    print("better luck next time😯")
    exit()
 ######################################
print(q3[0])
print(q3[1])
ans = input("enter your answer:")
if ans == "3":
    print("you have entered right answer!")
    print("you have won 30k")
    i = i+30
else:
    print("wrong answer!")
    exit()
########################################
print(q4[0])
print(q4[1])
ans = input("enter your answer:")
if ans == "2":
    print("you have entered right answer!")
    print("you have won 40k")
    i = i+40
else:
    print("wrong answer!")
    print("better luck next time😯")
    exit()
#################################################
print(q5[0])
print(q5[1])
ans = input("enter your answer:")
if ans == "1":
    print("you have entered right answer!")
    print("you have won 50k")
    i = i+50
    print("congratulations! you have won the game!")
else:
    print("wrong answer!") 
    print("better luck next time😯")
    exit()
##################################
print(f"To dosto aaj ke khel ke vijeta hai {name} ji!")
print(f"{name}ji ne jeete hain{i}k rupees!")
print("to aaj ka khel yahi samapt karte hai! fir milenge agle kehl main tabtak keliye alwida!☺☺☺☺☺☺☺☺")