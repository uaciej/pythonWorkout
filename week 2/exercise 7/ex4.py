'''
Given a string, URL-encode any character that isn’t a letter
or number. For the purposes of this exercise, we’ll assume that all characters
are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters.
'''

def url_encoder(sentence):
    for char in sentence:
        if not char.isalnum():
            yield f"%{hex(ord(char))[2:]}"
        else:
            yield char






    
if __name__ == "__main__":
    article = "The authors of this paper are John Doe and Jane Smith. They argue that being short migh lead to self esteem issues and noticed a spike in depression in male subjects below 6 feet."
    encoded_string = "".join(url_encoder(article))
    print(encoded_string)