'''
In this exercise, I want you to write a get_sv function that returns a set of all
“supervocalic” words in the dict. If you’ve never heard the term supervocalic before,
you’re not alone: I only learned about such words several years ago. Simply put, such
words contain all five vowels in English (a, e, i, o, and u), each of them appearing
once and in alphabetical order.
 For the purposes of this exercise, I’ll loosen the definition, accepting any word that
has all five vowels, in any order and any number of times. Your function should find all
of the words that match this definition (i.e., contain a, e, i, o, and u) and return a set
containing them.
Your function should take a single argument: the name of a text file containing
one word per line, as in a Unix/Linux dict.
'''

def get_sv(file):
    with open(file) as f:
        return {word for line in f for word in line.split() if set('aeiou') < set(word.lower())}


if __name__ == "__main__":
    print(get_sv('../assets/words.txt'))