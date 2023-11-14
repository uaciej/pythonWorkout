import random
from english_words import get_english_words_set

def make_dictionary():
    web2lowerset = get_english_words_set(['web2'], lower=True)
    web2lower = list(filter(lambda x: len(x) <= 5, web2lowerset))
    web2lower.sort()
    return web2lower

def guessing_game():
    dictionary = make_dictionary()
    num = random.randint(0, len(dictionary))
    word = dictionary[num]
    while True:
        userWord = input("Guess the word: ")
        if len(userWord) > 5:
            print("That's too long! Try again.")
            continue
        elif userWord == word:
            print('Correct!')
            break
        elif userWord not in dictionary:
            print("Not a word")
            continue
        elif dictionary.index(userWord) > num:
            print("The word is earlier in the dictionary")
        elif dictionary.index(userWord) < num:
            print("The word is later in the dictionary")

if __name__ == "__main__":
    guessing_game()
