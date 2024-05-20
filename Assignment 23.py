#Get number from user and reverse number in other variable and print output

number = int(input("enter any number"))
rev_num = 0
original_number = number

while number !=0:
    digit = number % 10
    rev_num = rev_num * 10 + digit
    number //= 10

print(f"the reverse of {original_number} is: {rev_num}")
