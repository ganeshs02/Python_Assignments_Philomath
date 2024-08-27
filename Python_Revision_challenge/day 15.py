# make a program which takes the input form the user and also take the user
# choice to encode,deocde or exit out of the program.

words = input("choose the fascility you want to use :encode, decode, exit: ")

#encode

if words ==  "encode":
    final = []
    words = input("enter the word you want to encode:")
    words = words.split(" ")
    for word in words:
        if len(word)>= 3:
            r1 = "xyz"
            r2 = "abc"
            stage1 = r1 + word[1::] + word[:1] + r2
        
            final.append(stage1)
        else:
            final.append(word[::-1])
    print(" ".join(final))

#decoding
elif words == "decode":
    final = []
    words = input("Enter the text you want to decode: ")
    words = words.split(" ")
    for word in words:
        if len(word) >= 9 and word.startswith("xyz") and word.endswith("abc"):
            stage1 = word[3:-3]  # Remove "xyz" from the start and "abc" from the end
            decoded = stage1[-1] + stage1[:-1]  # take the words from stage1 and add the last word to first index
            final.append(decoded)
        else:
            final.append(word[::-1])  # Reverse words with length < 3
    print(" ".join(final))  # Join the final list with spaces

#exit 
elif words == "exit":
    exit("exiting the program ...... thank you!")







