'''
Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized, but the rest of the word isn’t), then the Ubbi Dubbi translation should be
similarly capitalized.
'''

def ubbi_dubbi(word):
    output = []
    cap = False
    if word[0].isupper():
        cap = True
    for char in word.lower():
        if char in 'aeiou':
            output.append('ub' + char)
        else:
            output.append(char)
    if cap:
        return (''.join(output)).capitalize()
    
    return ''.join(output)



if __name__ == '__main__':
    word = input("Enter a word: ")
    print(ubbi_dubbi(word))