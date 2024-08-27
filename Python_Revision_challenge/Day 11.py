# fibonacci series code (recursion)

'''a = int(input("enter the no of steps you want to print:"))

def fibonacci (n):

    if n == 0 or n == 1: #basecase
        return n
    else:
        return (fibonacci(n - 1)) + (fibonacci(n-2)) #recrusive case
for i in range(a):
    print(fibonacci(i))       

print(fibonacci.__doc__)''' # function documentation

#in this program the recursive approach is used.
#Recursion = Recursion is the process in which the function
#calls itself to solve a problem'''


#swapping of the two numbers without using third variable

'''
a = 10
b = 20

(a,b) = (b,a) 
print(a,b)
'''



# code to print factorials of the number(recursion)

'''n = int(input("enter the number to print the factors"))
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return(n*factorial(n-1))

print(factorial(n))'''



#sets  {} immutable
# unordered collection of the data items which are separated by the comma
# and enclosed in {} braces.

#example

ganesh = set()
ganesh = { } #empty set becomes dict

print(type(ganesh)) 

#set methods 

#1 set join
s1 =  {1,2,3,4,5,6}
s2 = {7,8,9,10,11}

print(s1.union(s2))

s2.update(s1)
print(s2)
print(s1, s2)

#2 set intersection 
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)


#3 symmetric difference  (prints cities which are not common)

cities = {"mumbai", "ohio", "banglore", "bhopal"}
cities2 = {"satara", "mumbai", "chennai", "ohio"}
citeis3 = cities.symmetric_difference(cities2)
print(citeis3)


#4 disjoint set (sets which donot have any element common)

print(cities.isdisjoint(cities2))

#5 superset(previous set has elements of nest set)

print(cities.issuperset(cities2))

#6 Add (to add element in set)

cities.add ("prayagraj")
print(cities)

#7 remove

cities.remove("bhopal")
print(cities)

#8 discard (to dump element)
cities.discard("mumbai")
print(cities)


#9 pop (to pop any random element from set)
item = cities.pop() #pops first element
print(cities)
print(item)

#10 clear(to delete all elements in the set)
city = cities.clear


#11 del (to delete entire set)
del cities
#print(cities)

#12 "in" keyword ("to search if item present inset")

if "ohio" in cities2:
    print("ohio present")
else:
    print("ohio absent")