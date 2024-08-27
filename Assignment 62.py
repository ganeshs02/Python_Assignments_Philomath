#Ask user to enter 2 lists of 5 elements each
# (user should enter as comma separated string),
# generate lists from the strings and check if two lists entered by user
# are same

string1 = input("enter any string with 5 elements separated by comma ")

string2 = input("enter any string with 5 elements separated by comma ")

def check(string1,string2):
    string12 = string1.split(',')
    string22 = string2.split(',')
    if len(string12) and len(string22) != 5:
        print("The string you entered is above or below 5 words!")
    elif string12 == string22:
        print("The string you provided are matching!")
    else:
        print("The string you provided is not matching!")

check(string1,string2)


