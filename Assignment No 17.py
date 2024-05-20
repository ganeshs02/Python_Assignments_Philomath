#get a number from user, write a program to check if number is prime number

number = int(input("enter the number:"))

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
    

if is_prime(number):
    print(number, "is a prime number: ")

else:
    print(number, "is not a prime number :")


