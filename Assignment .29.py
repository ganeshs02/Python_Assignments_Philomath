'''
"29","print patterns -- madhura to fill this",
"29_Assignmentloops","loops","","","","","","","","","",""
*
* *
* * *
* * * *
* * *
* *
*
'''


n=4
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range (n+1):
    for j in range(n-i,0,-1):
        print("*", end=" ")
    print()


