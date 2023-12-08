'''
Take a text file, creating (and printing) a nonsensical sentence from the nth
word on each of the first 10 lines, where n is the line number
'''

with open('text.txt', 'r') as text_file:
    sentence = ''
    n = int(input('Which word should be picked? '))
    for row in text_file:
        words = row.split()
        try:
            sentence += words[n] + ' '
        except:
            continue
    
    print(sentence)