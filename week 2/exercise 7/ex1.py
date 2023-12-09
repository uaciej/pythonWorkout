'''
 For this exercise, you’ll write a function (called ubbi_dubbi) that takes a single
word (string) as an argument. It returns a string, the word’s translation into Ubbi
Dubbi. In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub.
'''

def ubbi_dubbi(word):
    output = []
    for char in word:
        if char in 'aeiou':
            output.append('ub' + char)
        else:
            output.append(char)

    return ''.join(output)



if __name__ == '__main__':
    word = input("Enter a word: ")
    print(ubbi_dubbi(word))