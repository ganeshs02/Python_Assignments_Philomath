#short hand if-else - it can be convienient to write a simple if -else statement using it.
#when you want to assign value variable based on condition 
'''but it is not suitable for the complex situations'''

#example 1

a = 10
b = 20

print("x") if a<b else print("a") if a == b else print("c")
# it can be used in the less complex situations

########

#example 2
c = 9 if a>b else 0
print(c)


#######################################################

# enumarate function -built in function which allows you to the loop 
#over a sequence such as list tuple or string and get index and value of each element in the 
#sequence at the same time


#1 example 

marks = [12.56, 32, 98, 12, 45, 1, 4]

index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("harry,awesome!")
    

#example 2 -using enumarate function we can enumarate directly .

for index,mark in enumerate(marks, start=1):
    print(mark)
    if (index == 3):
        print("awesome,ganesh!")


#example 3 - 

fruits = ["apple", "banana", "cherry", "date"]

# Using enumerate to get the index and value
for index, fruit in enumerate(fruits, start=2):
    print(f"Index {index}: {fruit}")
