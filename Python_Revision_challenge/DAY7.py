#Functions
#1 inbuilt functions and #2 Userdefined functions

#inbuilt functions - mean,add,range

#userdefined functions- 
#it can be called any time
#1 to find mean 

def geometric(a,b):
    mean = ((a*b)/(a+b))
    print(mean)

#2 to add numbers 

def plus(a,b):
    plus = (a+b)
    print(plus)


#3 to find greater number

def greater(a,b):
    if(a>b):
        print(a,"is greater")
    else:
        print(b,"is greater")

#4 to create function to define later

def abhinandan(a,b):
    pass


###########################
a = 10
b = 20

geometric(a,b)
plus(a,b)
greater(a,b)

c = 90
d = 100

geometric(c,d)
plus(c,d)
greater(c,d)





