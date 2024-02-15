'''
 Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace
surrounded by whitespace) that contain only integers, and sum them.
'''


def sum_the_ints(file):
    
    with open(file, 'r') as f:
        out = 0
        for line in f:
            words = line.split()
            for word in words:
                if word.strip().isdigit():
                    out += int(word)
    
    return out

if __name__ == "__main__":
    print(sum_the_ints('../text.txt'))