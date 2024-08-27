#start with hard coded list say a = [12,3,34,45,88,23,45,63,3,4,69,99],
# get two numbers from user, store them in second list. Write a program to check if
# sencond list is subset of first list. Print the output

firstlist = [12,3,34,45,88,23,45,63,3,4,69,99]

sublist = input("ente two numbers with spcees:").split()

num1 = int(sublist[0])
num2 = int(sublist[1])

if num1 and num2 in firstlist:
    print(f"{num1} and {num2} are subset of the first list, {firstlist}")
else:
    print(f"{num1} and {num2} are not subset of the firstlist")
