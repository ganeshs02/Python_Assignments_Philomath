# ask user to enter a sentence, store sentence as list of words.
# Enter another word from user and write a function to findout number of
# occurances of the word in the sentence.


sentence = input("enter the sentence: ")
word = input("enter any word in the string:")
count = 0


def counting(word, sentence):
    global count
    for words in sentence.split():
        if words == word:
            count += 1
            print(count)



counting(word, sentence)
print(f"the word has occured : {count} times in the sentence.")
