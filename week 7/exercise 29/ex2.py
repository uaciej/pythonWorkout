'''
 Show the lines of a text file that contain at least one vowel and contain more
than 20 characters.
'''

def show_lines(file):
    with open(file) as f:
        return [line.rstrip('\n') for line in f if set('aeiou').intersection(set(line)) and len(line)> 20]



if __name__ == '__main__':
    print(show_lines('../assets/bruh.txt'))