#A class called book, attributed should include: Author, Title, Genre, and Year Published. The class should have a method that returns a string with the book's information formatted nicely.
class Book:
    def __init__(self, author: str, title: str, genre: str, year_published: int):
        self.author = author
        self.title = title
        self.genre = genre
        self.year_published = year_published

    def get_info(self):
        return f"'{self.title}' by {self.author} ({self.year_published}) - {self.genre}"

#Pull some books from the library and print their information
book_1 = Book("Jane Doe", "Illeterate Book", "Psychological", 2000)
print(book_1.get_info())

book_2 = Book("John Doe", "This Book Is Not Poo", "Fantasy", 1997)
print(book_2.get_info())