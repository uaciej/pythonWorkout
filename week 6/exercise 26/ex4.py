'''
 Write a function, transform_lines, that takes three arguments: a function that
takes a single argument, the name of an input file, and the name of an output
file. Calling the function will run the function on each line of the input file,
with the results written to the output file. (Hint: the previous exercise and this
one are closely related.) 
'''

def transform_lines(func, in_file, out_file):
    with open(in_file) as f_in, open(out_file, 'w') as f_out:
        for line in f_in:
            f_out.writelines(func(line))


if __name__  == '__main__':
    transform_lines(lambda x: 'Bruh ' + x, '../assets/text.txt', '../assets/text_transformed.txt')