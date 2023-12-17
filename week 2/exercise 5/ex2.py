'''
Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized, but the rest of the word isn't), then the Pig Latin translation should be
similarly capitalized.
'''

def pig_latin(word):
    if word[0].lower() in 'aeiou':
        return word + "way"
    elif word[0].isupper():
        return (word[1:] + word[0] + 'ay').capitalize()
    else:
        return word[1:] + word[0] + 'ay'
    
if __name__ == '__main__':
    print(pig_latin(input('What word would you like to translate? ')))