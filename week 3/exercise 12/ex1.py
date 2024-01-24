'''
Write a function, most_repeating_word, that takes a sequence of strings as input. The
function should return the string that contains the greatest number of repeated letters.
'''
from collections import Counter

def most_repeating_word(words):
    the_word = ''
    count = 0
    for word in words:
        letter_count = Counter(word).most_common(1)[0][1]
        if letter_count > count:
            count = letter_count
            the_word = word

    return the_word


if __name__ == "__main__":
    words =  ['this', 'is', 'an', 'elementary', 'test', 'example']
    print(most_repeating_word(words))