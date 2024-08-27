#Operator overloading 
'''operator overloading is a feature in python that allows developers to redefine the 
behaviour of the mathematical and comaprison operatings for custom data types . That means 
you can use (=, -, *, / . etc) and (>,<,== etc) in your classes just as you would use for 
built in data types int and str'''

#operator overloading allows you to create more readable and initiative code for instance

#Example 1

class vector:
    def __init__ (self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__ (self):
        return f"{self.i}i + {self.j}j + {self.k}k" #fstring to print vector format
    
    def __add__(self, x):
        return vector(self.i + x.i, self.j + x.j,self.k + x.k) #to get the result in the vector format
    


v1 = vector(5,5,5)
print(v1)
print(type(v1)) #<class '__main__.vector'>

v2  = vector(4,2,8)
print(type(v2)) #<class '__main__.vector'>

print(v1+v2) #it adds the two vectors and return in the vector format also
print(type(v1+v2)) #<class '__main__.vector'>



#single inheritance 
'''Single inheritance is a type of inheritance where a class inherits the methods and properties of
single parent class , this is simplest and most common inheritance'''


'''syntax  class omnivorus (animal): #inherited by animal class
            #class body             '''


#example 1

class animal:
    def __init__ (self,name,species):
        self.name = name
        self.species = species

    def makesound(self):
        print(f"hello my name is {self.name}")


class dog(animal): #dog subclass inherited by animal parent class
    def __init__ (self,name,breed):
        animal.__init__(self,name,species = "dog")
        self.breed = breed
    def makesound(self): #method overriding 
        print("bark")


a1 = animal("rabbit", "herbivorous")

a1.makesound()


d1 = dog("dhruv","German")
d1.makesound()


#implement a cat class by using the animal class
#add some specific methods to cat

class cat(animal):
    def __init__ (self,name,specices):
        animal.__init__(self, name ,species="cat")
        self.species = specices

    def makesound(self):  #method overloading
        #return super().makesound() '''to return the parent class method'''
        print("mewww!")


    def makeangry(self):
        print("purr")


c1 = cat("lisa", "persian")
c1.makeangry()
c1.makesound()
print(c1.name)
