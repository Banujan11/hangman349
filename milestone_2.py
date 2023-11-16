import random


Word_list= ['apple', 'banana', 'pear','cherry', 'mango']
print(Word_list)
word = random.choice(Word_list)
print(word)

guess = input("Please enter a single alphabectical character: ")
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else: 
    print("Oops! That is not a valid input.")