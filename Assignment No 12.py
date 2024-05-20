#Ask user to enter name, age and address and let user know if user can do voting.

name = input("enter your name:")
age = input("enter your age:")
address = input("enter your address:")


if int(age) > 18 or age==18:
    print("hello Congratulations Mr."+name+"you are eligble for voting")

else:
    print("hello Sorry Mr."+name+"your are not eligible for voting")


