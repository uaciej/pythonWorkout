'''
 Given a string containing several (space-separated) words, create a dict in which
the keys are the words, and the values are the number of vowels in each word. If
the string is “this is an easy test,” then the resulting dict would be {'this':1,
'is':1, 'an':1, 'easy':2, 'test':1}.
'''

def dic_words_len(sentence):
    return {word : len(word) for word in sentence.split()}



if __name__ == "__main__":
    print(dic_words_len('Tax fraud is underwhelming if you get caught'))