#"numbers and alphabets: assign 3 alphabets for each digit between 0 and 9.
# Write a program to write all possible codes that can be generated for any user entered number.
#For example: 1 - a,b,c and 2 - d,e,f then number 12 can be made as any of the
# codes: ad,ae,af,bd,be,bf,cd,ce,cf.
for itertools import product

digit_to_letters = {
    '1' : ['a','b','c'],
    '2' : ['e', 'f','g'],
    '3' : ['h','i','j'],
    '4' : ['k','l','m'],
    '5' : ['n','o','q'],
    '6' : ['r','s','t'],
    '7' : ['u','v','w'],
    '8' : ['x','y','z'],
    '9' : ['m','p','d']}


number = input("enter the number:")

codes= generate_codes(number)
print("possible codes are:")
for code in codes:
    print(code)