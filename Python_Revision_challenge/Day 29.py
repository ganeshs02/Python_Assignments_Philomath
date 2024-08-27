#Method Overriding - 
'''Method overriding in python is Powerful feature in object oriented programming which allows
you to redefine a method in derived class the method in the derived class is said to override 
the method in the base class whe you create an instance of the derived class and call the 
override method the version of the method in the derived class is executed rather than the version 
in the base class '''

#it is way to customize the behaviour of the passed method on its specific neeeds.

#example 1 

class Shape: #parent class
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def area(self): #method to be overriden
        return self.x * self.y
    
class Circle(Shape): #Child class inherited by (Shape)
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius) #we used and changed 'x' and  'y' values here by radius (method overriden)
    def area(self):
        return 3.14 * super().area() #we currently using the 'area' method in parent class (r*r)
    

rec = Shape(30,60) #area of rectangle ,#actual formula
print(rec.area())

rec2 = Circle(4) #here we need only one value cause we used one 'radius' in init. #overriden formula
print(rec2.area())

rec3 = Circle(5)
print(rec3.area())
    