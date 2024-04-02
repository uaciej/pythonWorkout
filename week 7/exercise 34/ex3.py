'''
Given a text file, what are the lengths of the different words? 
Return a set of different word lengths in the file.
'''

def get_len(file):
    with open(file) as f:
        return {len(word) for line in f for word in line.split()}


if __name__ == "__main__":
    print(get_len('../assets/words.txt'))