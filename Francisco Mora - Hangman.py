import random
import string
automobiles = ["lamborghini", "bugatti", "corvette!", "ford", "ferrari", "porsche", "mclaren", "maserati", "scion",
               "tesla"]
output = []
guesses = 8

list_of_letters = string.ascii_letters

word_selection = random.choice(words)
length = len[word_selection]
word_list = list(word_selection)

for i in range(length):
    output.append("* ")
print("".join(output))

while guesses > 0 and len(word_list) > 0:
    user_guess = input("Guess a letter")
    print('\n * 10')
    if user_guess in word_selection:
        print("You are correct!")
        for i in range(len(word_selection)):
            if user_guess is word_list:
                word_list.pop(1)
        for i in range(len(word_selection)):
            if word_selection 