#Break and Continue statement 
#Break - for breaking execution after conditon is satisfied. 
#continue - continues loop until condition is true

#########
#EXCERCISE 1
#write the code to get the input from the user until user enters number 
#greater than 100.

'''inp = 0

while(True):
    inp = int(input("enter any integer \n"))
    if(inp>100):
        print("congrats you have entered number greater than 100")
        break #breaks the loop
    else:
        print("try again!")
        continue #continues loop over again
'''

#example

i = 0

while (True):
    if (i<40):
        print(i, end=" ")
        i = i+1
        continue
    elif (i == 100):
        print(i, end= " ")
        break
    else:
        print(i , end=" ")
        i = i+1
        
    
        