 # object oreinted programming  - using classes and objects to represent real world concepts and entities.

'''
class - class is and blueprint of the template for creating object it defines properties and methods
that an object of that class will have. properties are state of an object and methods are 
the actions or behaviour that object can perform

object -  object is and instance of an class and contains its own data and methods.
example - having class "person" and that has properties such as 'name' and 'age' and methods such as
speak() and walk () 

Encapsulation - it mean internal state of an object is hidden and can be only accessible by the object
methods which helps to protect objects data and prevent it for being modified in unexpected way.

inheritance - it allows new classes to be created that inherits the properties methods of an existing 
class (parent class) this allow for code reuse and maintain it easily create new class that have 
similar function to existing classes.

polymorphism - it supports in python which means that object of different classes can be created as
if they were object of common class. this allows for greater flexibility in code and makes it easier 
to write code that can work with multiple type of objects.


in short oops in python allows developers to model "real world concepts and entities using classes 
objects, encapsulate data , reuse code through inheritance and write more flexible code through 
polymorphism.

'''


#############################################################################################################
#practice -  make a snake water and gun game 


import random

def check(comp,user):
    if comp == user:
        return 0
    if comp == 0 and user == 1 :
        return -1
    if comp == 1 and user == 2 :
        return -1
    if comp == 2 and user == 0 :
        return -1
    return 1 


user = int(input("choose 0 for snake, choose 1 for water and choose 2 for gun:\n"))
comp = random.randint(0,2)

print(f"user : {user}")
print(f"computer:{comp}")

result = check(comp,user)

if result == 0:
    print("its an tie!")
elif result == -1:
    print("you lost !!")
else:
    print("you have won the match!")