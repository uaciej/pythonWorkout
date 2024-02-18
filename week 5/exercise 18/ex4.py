'''
 Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation. 
'''

def count_vowels(file):
    with open(file, 'r') as f:
        out = {i : 0 for i in "aeiou"}
        for line in f:
            for letter in line:
                if letter in 'aeiou':
                    out[letter] += 1
    
    return out

if __name__ == "__main__":
    print(count_vowels('../text.txt'))