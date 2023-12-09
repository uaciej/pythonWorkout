'''
Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a
way that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].
'''

def transpose(word_list):
    outcome = ['' for _ in word_list]
    for elem in word_list:
        elem = elem.split()
        first = True
        for i, word in enumerate(elem):
            outcome[i] += ' ' + word
            if first:
                outcome[i] = outcome[i].lstrip()
                first = False
    return outcome


if __name__ == "__main__":
    word_list = ['abc def ghi', 'jkl mno pqr', 'stu wvx yz']
    print(transpose(word_list))