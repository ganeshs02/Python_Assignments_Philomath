#ask user to enter a string, ask user to enter a character,
# write a program to check number of occurances of that character in the string given by user.

string = input("enter any sentence")
string1 = string.replace(" ","")
character = input("enter any character")
count = 0
string1chars = []
for chars in string1:
    string1chars.append(chars)

for char in character:
    if char in string1chars:
        count += 1

print(f"the charcter '{character}' occured in the input sting , '{count}' times ")




