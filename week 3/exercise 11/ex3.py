'''
Given a list of strings, sort them according to how many vowels they contain.
'''

def sort_strings_by_vowel_amount(strings):
    def count_vowels(string):
        return sum(1 for char in string if char.lower() in 'aeiou')
    return sorted(strings, key=count_vowels, reverse=True)


if __name__ == "__main__":
    strings = ['A', 'aa', 'aAa', 'lmao', 'banana', 'bananas', 'audiophonic']
    print("Original List: ", strings)
    print("Sorted List: ", sort_strings_by_vowel_amount(strings))