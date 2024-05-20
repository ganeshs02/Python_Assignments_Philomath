#get three sides of a triangle from user and check if that is a valid triangle

side1 = int(input("enter the side1 of the triangle"))
side2 = int(input("enter the side2 of the triangle"))
side3 = int(input("entter the side3 of the traingle"))

if side1+side2 > side3:
    print("this is the triangle")

else:
    print("this is not the triangle.")
