'''
 Which is the last word, alphabetically, in a text file?
'''

def last_word(text):
    words = text.split()
    return sorted(words)[-1]

with open('text.txt', 'r') as text_file:
    print(last_word(text_file.read()))
