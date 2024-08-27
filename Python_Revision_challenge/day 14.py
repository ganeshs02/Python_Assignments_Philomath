#make a program which will encode and decode the message between the 2 persons.


words = input("choose the fascility from the following : encode, decode, exit:")

#encode 
if words == "encode":
    final = []
    words = input("enter the text you want to encode:")

    words = words.split(" ")
    for word in words:
        if len(word) >= 3:
            r1 = "xyz"
            r2 = "abd"
            stage1 =  r1 + word[1: ] + word[0] + r2 #encoded the word having more than 3 words
          
            final.append(stage1)
        else:
            final.append(word[::-1]) # reversed the word less than 3 letters
    print(final)

 #decode 
if words == "decode":
    final = []
    words = (input("enter you message for decoding:"))
    words.split(" ")
    print(words)



