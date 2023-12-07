'''
Consider an alternative version of Pig Latin—We don’t check to see if the first letter
is a vowel, but, rather, we check to see if the word contains two different vowels.
If it does, we don’t move the first letter to the end. Because the word “wine”
contains two different vowels (“i” and “e”), we’ll add “way” to the end of it, giving us “wineway.” By contrast, the word “wind” contains only one vowel, so we
would move the first letter to the end and add “ay,” rendering it “indway.” How
would you check for two different vowels in the word?
'''

def pig_latin(word):
    word = word.lower()
    word_set = set(word)
    common = [x for x in 'aeiou' if x in word_set]
    if len(common) == 1:
        return word[1:] + word[0] + 'ay'
    elif len(common) > 1:
        return word + 'way'
    else:
        return word
    
if __name__ == '__main__':
    print(pig_latin(input('What word would you like to translate? ')))