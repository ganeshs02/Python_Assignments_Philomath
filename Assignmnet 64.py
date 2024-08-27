#Ask user to enter two strings as command line arguments and check if
# 2nd string is subset of 1st string without using string functions.


string1 = input("enter the string parent string:")

string2 = input("enter the child string:")


def subset(string1,string2):

    string12 = string1.split()
    string22 = string2.split()
    for word in string22:
        if word not in string12:
            print("the second string is not an subset of first string!")
            return

    print("the second string is the subset of the first string!")




subset(string1,string2)


