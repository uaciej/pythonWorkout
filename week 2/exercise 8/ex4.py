'''
 Which is the longest word in a text file?
'''
import string

def longest_word(text):
    # Make a translator that replaces punctuation with empty character (faster for long strings than .replace)
    translator = str.maketrans('', '', string.punctuation)
    # Remove punctuation from text and split into separate words
    words = text.translate(translator).split()
    
    return sorted(words, key= lambda x : len(x))[-1]


with open('text.txt', 'r') as text_file:
    print(longest_word(text_file.read()))
