'''
Create a Book class that lets you create books with a title, author, and price.
Then create a Shelf class, onto which you can place one or more books with an
add_book method. Finally, add a total_price method to the Shelf class, which
will total the prices of the books on the shelf
'''

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Shelf:
    def __init__(self):
        self.bookshelf = []

    def add_book(self, *books):
        for book in books:
            self.bookshelf.append(book)

    def total_price(self):
        return sum(b.price for b in self.bookshelf)
    

if __name__ == "__main__":
    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 20.00)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 15.50)
    book3 = Book("1984", "George Orwell", 19.84)
    book4 = Book("Conteplating suicide with PHP", "Mariusz Dąbal", 69.42)
    s = Shelf()
    s.add_book(book1, book2, book3, book4)
    print(s.total_price())
