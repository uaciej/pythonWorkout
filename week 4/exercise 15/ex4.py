'''
 Read through a text file on disk. Use a dict to track how many words of each
length are in the file—that is, how many three-letter words, four-letter words,
five-letter words, and so on. Display your results. 
'''

def count_letters(file):
    with open(file, 'r') as f:
        word_count = {}
        for line in f:
            words = line.split()
            for word in words:
                word_count[len(word)] = word_count.get(len(word), 0) + 1

        for word_len, count in sorted(word_count.items()):
            print(f'{word_len}-letter words : {count}')


if __name__ == "__main__":
    count_letters('text.txt')