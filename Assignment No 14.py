#Ask user to enter number if number is in 1s then print one, if number is in 10s then print ten if number is in 100s then print hundred if number is in 1000 print thousand. (try to implement this using if-elif-else

Number = (input("enter the number :"))

if len(Number)== 1:
    print("one")
elif len(Number)== 2:
    print("ten")
elif len(Number)== 3:
    print("hundread")
else:
    print("Thousand")




