'''
Handle punctuation—If a word ends with punctuation, then that punctuation
should be shifted to the end of the translated word.
'''

def pig_latin(word):
    punct = ''
    if word[-1] in '.,?!:;':
        punct = word[-1]
        word = word[:-1]
    if word[0].lower() in 'aeiou':
        return word + "way" + punct
    elif word[0].isupper():
        return (word[1:] + word[0].lower() + 'ay').capitalize() + punct
    else:
        return word[1:] + word[0] + 'ay'+ punct
    
if __name__ == '__main__':
    print(pig_latin(input('What word would you like to translate? ')))