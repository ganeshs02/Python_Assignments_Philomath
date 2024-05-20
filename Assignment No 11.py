#ask user to enter name and surname and concatenate name and surname,  print name and surname in lower case if name starts with b other wise pri0nt name in title case

name = str(input("enter your name:"))
surname = str(input("enter your last name:"))

full_name = name + " " +surname

if name.lower().startswith('b'):
   print("Name and surnmae in lowercase:", full_name.lower())

else:
   print("Name and surname in title case:", full_name.title())


