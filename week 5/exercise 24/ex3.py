'''
Given an existing text file, create two new text files. The new files will each contain the same number of lines as the input file. In one output file, you’ll write
all of the vowels (a, e, i, o, and u) from the input file. In the other, you’ll write
all of the consonants. (You can ignore punctuation and whitespace.)
'''

def split_file_content(input_file, output_file1, output_file2):
    with open(input_file,'r') as inf, open(output_file1, 'w') as outf1, open(output_file2, 'w') as outf2:
        for line in inf:
            for char in line:
                if char.lower() in 'aeiou':
                    outf1.write(char)
                elif not char.isalpha():
                    continue
                else:
                    outf2.write(char)
            outf1.write('\n')
            outf2.write('\n')


if __name__ == "__main__":
    split_file_content('../text.txt', '../split_text1.txt', '../split_text2.txt')