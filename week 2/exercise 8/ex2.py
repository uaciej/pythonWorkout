'''
Given the string “Tom Dick Harry,” break it into individual words, and then sort
those words alphabetically. Once they’re sorted, print them with commas (,)
between the names.
'''

def string_sort(sentence):
    words = sentence.split()
    for word in words:
        new_word = ''.join(sorted(word))
        yield new_word



if __name__ == "__main__":
    sentence = "Tom Dick Harry,"
    print(','.join(string_sort(sentence)))