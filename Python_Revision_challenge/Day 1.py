#excercise 1 
'''no1 = int(input("enter the first number"))
no2 = int(input("enter the second number"))

print(f"the sum of the two numbers is\n", no1 + no2)#newline character
'''
#excercise 2
#string #immutable
'''string1 = "hello my name is ganesh"

print(string1[::-1])
print(string1[::])
print(len(string1))
print(string1[2])
print(string1[0:555])
print(string1.isalnum())
print(string1.isalpha())
print(string1.endswith("ganesh"))
print(string1.count("g"))
print(string1.capitalize())
print(string1.find("i"))
print(string1.lower())
print(string1.upper())
print(string1.replace("ganesh","hanuman"))'''

#list #mutable
'''
numbers = [1,2,3,4,5,6,7,8,9]

print(numbers)
print(numbers[1:4])
print(numbers[:])
numbers.append(55)
print(numbers)
numbers.insert(1,5)#index,number
print(numbers)
numbers.remove(7)#number to be removed
print(numbers)'''

# Tuple  #immutable

'''partners = (1,2,3,4)
print(partners)

print(type(partners))
'''
#excercise 3 #swapping two numbers without using third variable

'''a = 10
b = 20 

a,b = b,a 

print(a,b)'''


# Dictioary #mutable
'''
d1 = {"ganesh":"rolls royace", "pratham": "nano", "nishad": "bajaj"}

print(d1)
print(type(d1))

d1["kiran"] = "maserati" #adding values into dictionary
print(d1)

del d1["pratham"] #to delete element
print(d1)

print(d1["ganesh"]) #to print perticular element

# functions in dict

print(d1.get("ganesh"))

d2 = d1.copy #to make duplicate dict
print(d1)

d1.update({"kali":"mali"}) #to add element
print(d1)

print(d1.keys()) #key

print(d1.items()) #key value

'''
## Dictionary execercise
#create a dictionary and take input form the user and return the 
#meaning

'''dic2 = {"modi":"pm", "pappu":"rahul","mamta":"hamba"}
inp1 = input("enter the name:")

print(dic2.get(inp1)) #dictionary is not callable

'''
#################
#set  #mutable 

s = set("hello") #it retains only unique values not double
print(s)
s.add("dj")
print(s)

print(s)
print(len(s))

s1 = s.union({1,2,3,}) #takes set s and adds values 1,2,3
print(s1)

s2 = s.intersection({1,2,3,"h"}) #takes set s and prints only common values
print(s2)


################### Data types completed ########################
'''
mutable - dict , list ,set
immutable - tuple , string'''