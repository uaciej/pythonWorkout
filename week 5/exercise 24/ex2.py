'''
 “Encrypt” a text file by turning all of its characters into their numeric equivalents (with the built-in ord function) and writing that file to disk. Now “decrypt”
the file (using the built-in chr function), turning the numbers back into their
original characters.
'''

def encrypt_file_content(input_file, output_file):
    with open(input_file,'r') as inf,  open(output_file, 'w') as outf:
        for line in inf:
            for char in line:
                outf.write(str(ord(char)))
                outf.write(' ')
            outf.write('\n')

def decrypt_file_content(input_file, output_file):
    with open(input_file,'r') as inf,  open(output_file, 'w') as outf:
        for line in inf:
            for num in line.split():
                outf.write(chr(int(num)))

if __name__ == "__main__":
    encrypt_file_content('../text.txt', '../encrypted_text.txt')
    decrypt_file_content('../encrypted_text.txt', '../text2.txt')