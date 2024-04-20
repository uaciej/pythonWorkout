'''
Create a list of tuples in which each tuple contains three elements: (1) the
author’s first and last names, (2) the book’s title, and (3) the book’s price in
U.S. dollars. Use a dict comprehension to turn this into a dict whose keys are
the book’s titles, with the values being another (sub-) dict, with keys for (a) the
author’s first name, (b) the author’s last name, and (c) the book’s price in
U.S. dollars
'''

books_info = [
    (("Jane", "Austen"), "Pride and Prejudice", 12.99),
    (("F. Scott", "Fitzgerald"), "The Great Gatsby", 10.50),
    (("Harper", "Lee"), "To Kill a Mockingbird", 14.95),
    (("George", "Orwell"), "1984", 9.75),
    (("J.K.", "Rowling"), "Harry Potter and the Sorcerer's Stone", 17.99)
]

def tuplis_to_dic(tuplis):
    return {book[1] : {'first_name' : book[0][0], 'last_name' : book[0][1], 'price' : book[2]} for book in tuplis}

books_dic = tuplis_to_dic(books_info)


if __name__ == "__main__":
    print(books_dic)