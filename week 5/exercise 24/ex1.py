'''
In many cases, we want to take a file in one format and save it to another format. In
this function, we do a basic version of this idea. The function takes two arguments: the
names of the input file (to be read from) and the output file (which will be created)
'''

def reverse_file_content(input_file, output_file):
    with open(input_file,'r') as inf,  open(output_file, 'w') as outf:
        for line in inf:
            outf.writelines(line[::-1])



if __name__ == "__main__":
    reverse_file_content('../text.txt', '../reversed_text.txt')