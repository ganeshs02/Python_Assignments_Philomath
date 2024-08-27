#ask user to enter a sentence and write a function to count number of words in
# the sentence.

sentence = input("enter any sentence :")
count = 0

def wordcount(sentence):
    print(len(sentence.replace(" ","")))

wordcount(sentence)
