"""get a number from user and check number of occurrences of a single digit in that number.
 (for example. Num=7888, check number of occurrences of digit 8 in number)"""

number = int(input("enter any number of your choice:"))
digit = int(input("enter the digit you want to count:"))
count = 0

while number > 0:
    tmp = number % 10
    number = number // 10
    if tmp == digit:
        count += 1

        print("digit:",digit, "came:", count, "times in the number")
