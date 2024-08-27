#ask user to enter a string and check if the string is a palindrom


input1 = input("enter any sentece:")


def pallindrome(input1):
    input12 = input1.replace(" ","")
    input1rev = input12[::-1]


    if input1rev == input12:
        print("the string you provided is an pallndrome!")
    else:
        print("the string you provided is not a pallindrome")
    print(input1rev)
pallindrome(input1)






