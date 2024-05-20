#Get number from user and reverse number in other variable and print output

number = int(input("enter the number"))

reversed_number = 0

while number != 0:

    digit = number % 10
    reversed_number=reversed_number*10+digit
    number = number // 10


print("the reversed number is :", reversed_number)