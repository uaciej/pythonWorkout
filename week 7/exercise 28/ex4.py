'''
Use a list comprehension to reverse the word order of lines in a text file. That
is, if the first line is abc def and the second line is ghi jkl, then you should
return the list ['def abc', 'jkl ghi'].
'''

def reverse_words(file):
    with open(file) as f:
        return [line.rstrip('\n')[::-1] for line in f]


if __name__  == "__main__":
    print(reverse_words('../assets/text.txt'))