#ask user to enter a word, write a function to count number of
# vovels in the word

word1 = input("enter any word of your choice:").lower()

vowels = 'aeiou'
count = 0

def vowelscout(word1, vowels):
    global count
    for word in word1:
        if word in vowels:
            count += 1
vowelscout(word1,vowels)
print(f"in the word you entered the vowels are occurred:{count}, times")