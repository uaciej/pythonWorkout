'''
The challenge for this exercise is to write a wordcount function that mimics the wc
Unix command. The function will take a filename as input and will print four lines
of output:
1 Number of characters (including whitespace)
2 Number of words (separated by whitespace)
3 Number of lines
4 Number of unique words (case sensitive, so “NO” is different from “no”)
'''

def word_count(file):
    with open(file, 'r') as f:
        number_of_characters = 0
        number_of_words = 0
        number_of_lines = 0
        words_set = set()
        for line in f:
           number_of_lines += 1
           number_of_characters += len(line)
           words_in_line = line.split()
           number_of_words += len(words_in_line)
           for word in words_in_line:
               words_set.add(word)
    
    return (f"Number of characters: {number_of_characters}\nNumber of words: {number_of_words}\nNumber of lines: {number_of_lines}\nNumber of unique words: {len(words_set)}")



if __name__ == "__main__":
    print(word_count("../wcfile.txt"))