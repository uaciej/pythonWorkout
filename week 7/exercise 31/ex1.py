'''
In this exercise, I want you to write a function that takes a filename as an argument. 
It returns a string with the file’s contents, but with each word translated into Pig
Latin, as per our plword function in chapter 2 on “strings.” The returned translation
can ignore newlines and isn’t required to handle capitalization and punctuation in
any specific way
'''

def plword(filename):
    with open(filename) as f:
        return ''.join(word + "way " if word[0].lower() in 'aeiou' 
                        else (word[1:] + word[0] + 'ay ').capitalize() if word[0].isupper() 
                        else word[1:] + word[0] + 'ay ' 
                        for line in f for word in line.split())



if __name__ == "__main__":
    print(plword('../assets/bruh.txt'))
