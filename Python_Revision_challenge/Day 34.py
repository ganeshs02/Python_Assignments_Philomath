# Generators in Python - 
'''Generators in python are special type of function that allow you to create an inheritable
sequence of the values a generator function returns a generator object which can be useful 
to (generate the values one-by-one as you iterate over it generators are pwoerful tool for
working with an larger complex data sets) as they allow you to generate values "one the fly" rather
than having to create and store entire sequence in memory)'''

#Generator can be created using "yeild" statement in function it retruns value of generator and 
#suspends execution until further value is requested.

#once you created it you can use it variety of the ways for loop,comprehension,generators expression.

#it is benificial over using 'lists,tuple and sets' cause generatos produce values on the go

#another benifits of the generator is they are 'lazy' that you generate value only when you need it

'''it is a powerful tool for working with loarge or complex data sets allowiing you to generate
that values on the fly and share only when you need them.'''

#Example 1 

def my_generator():
    for  i in range (500):
        #print(i) it will generate values directly
        yield(i) #it will generate as per need

gen = my_generator()

print(next(gen)) #to print the next value
print(next(gen))
print(next(gen)) #the value gets generated only when it is called.

#########################################################################################

#function caching -

'''function caching is a technology for imporoving the performance of the program by stoaring
the results of the function call so that you can reuse them every time the function calls 
this can be perticulary useful when a fuction is computationally expensive when a function
is called.

it can be achieved using the 'functool' moudle which has 'lru_cache' decorator used to cache
the results of the function so that you can reuse them for instead computing them all the time
they called. '''

#basically it stores the previously generated value which will requires many times in 
# program rather than computing it again and again 

#but it also take stoarage for stoaring them.


#example 1 

from functools import lru_cache #to store cache memory (previously generated results.)
import time

@lru_cache(maxsize=None) #(to allocate cache)  public function 
def fx(n):
    time.sleep(5)
    return n*5


'''print(fx(1))
print("done for 1") #takes 5 secs 

print(fx(2))
print("done for 2") #takes 5 secs 

print(fx(5))
print("done for 5") #takes 5 secs 

print(fx(25))
print("done for 25") #takes 5 secs 

print(fx(2))
print("done for 2") #gets printed instantly cause its calculated previously

print(fx(5))
print("done for 5")''' #gets printed instantly cause its calculated previously

# TIP - only use when you know perticular values are going to be called multiple times.

############################################################
#Regular expressions in python - https://regexr.com/

import re #regular expr module

'''Regular expression or 'regs' for 'start' are a powerful tools for working with the strings
and text data in the python they allow you to match and manipulate strings based on patterns
making it easy to perform complex string expectations with just a few line of code'''

#basically helps to find the 'complex patterns' in the huge strings.

#Example 1 - 

pattern = "" #pattern you want to search 
pattern2 = r"[A-Z]+all"  #it checks all the words for match between A-z starting and ending 'tall' .

paragraph = "The Mall was bustling with activity, with shoppers streaming through the Hall adorned with festive decorations. Nearby, a Tall sculpture stood as a centerpiece, drawing the attention of passersby.At the end of the corridor, a small store called Xall offered quirky trinkets, while the Dall café served the most delightful pastries. The atmosphere was lively, with echoes of chatter and laughter filling the air, making the Mall a vibrant place to be."

#########################################################

match = re.search(pattern2, paragraph) #(search pattern , paragraph text)
print(match) #<re.Match object; span=(4, 8), match='Mall'>

# but re.search stops execution as the first match spotted.
##################

match2 = re.finditer(pattern2, paragraph) #for multiple results(all) available
for match in match2:
    #print(match) #returns all finds 
    print(paragraph[match.span()[0]:match.span()[1]]) #returns first 2 matches


print(dir(re))


#######################################################################################################
