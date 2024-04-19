'''
In this exercise, you’ll write two functions:
 gematria_for, which takes a single word (string) as an argument and returns
the gematria score for that word
 gematria_equal_words, which takes a single word and returns a list of those
dict words whose gematria scores match the current word’s score.
'''
import string


let_num_dic = {k:v for k,v in zip(string.ascii_letters, range(1,27))}


def gematria_for(word):
    return sum(let_num_dic[char] for char in word if char.islower())


word_dic = {word: gematria_for(word) for line in open('../assets/words.txt') for word in line.split()}


def gematria_equal_words(word):
    score = gematria_for(word)
    return [other_word for other_word in word_dic if word_dic[other_word] == score]


if __name__ == "__main__":
    user_word = input('What word should we check?: ')
    print('Word score: ', gematria_for(user_word))
    print('Words of equal score: ', gematria_equal_words(user_word))