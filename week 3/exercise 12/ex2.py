'''
Instead of finding the word with the greatest number of repeated letters, find
the word with the greatest number of repeated vowels.
'''

from collections import Counter

def most_repeating_vowels(words):
    the_word = ''
    count = 0
    for word in words:
        letter_count = Counter(char for char in word if char in 'aeiou').most_common(1)[0][1]
        if letter_count > count:
            count = letter_count
            the_word = word

    return the_word


if __name__ == "__main__":
    words =  ['this', 'is', 'an', 'elementary', 'test', 'example']
    print(most_repeating_vowels(words))