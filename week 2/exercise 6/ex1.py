'''
Now that you’ve successfully written a translator for a single English word, let’s make
things more difficult: translate a series of English words into Pig Latin. Write a function called pl_sentence that takes a string containing several words, separated by
spaces. (To make things easier, we won’t actually ask for a real sentence. More specifically, there will be no capital letters or punctuation.)
'''

def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'
    
def pl_sentence(sentence):
    words = sentence.split()
    translated_words = []
    for word in words:
        translated_words.append(pig_latin(word))

    return ' '.join(translated_words)

if __name__ == '__main__':
    print(pl_sentence(input("What sentence should we translate? ")))

