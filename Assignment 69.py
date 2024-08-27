# get a string from user and write a function to return 1st non-repeating
# character (if 1st character is not repeating then return -1)

string1 = str(input("enter any string:"))
def not_repeating(string1):
    n_repeating = " "
    index = -1
    if len(string1) == 0:
        print("the provided string is empty")
    for i in string1:
        if string1.count(i) == 1:
            n_repeating += i
            break
        else:
            index += 1
    if index == len(string1) - 1:
        print("all the characters in the string are repeating!")
        return 1
    else:
        print(f"the first non repeating character in the string is,{n_repeating}")
        return -1

print(not_repeating(string1))




