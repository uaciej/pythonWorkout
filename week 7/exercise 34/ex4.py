'''
 Create a list whose elements are strings—the names of people in your family.
Now use a set comprehension (and, better yet, a nested set comprehension) to
find which letters are used in your family members’ names. 
'''

def letters_used(lst):
    return {letter.lower() for letter in ''.join(lst)}



if __name__ == "__main__":
    family = ['Sylwia', 'Szymon', 'Jadwiga', 'Ewa', 'Marek', 'Krzysiu', 'Mariusz', 'Jakub']
    print(letters_used(family))