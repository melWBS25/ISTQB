
from book import Book
def test_book_creation():
    """Test: Ich kann ein Book Objekt erstellen"""
    title = "Python Testing"
    isbn = 978123456789
    author = "Max Mustermann"

    book = Book(title ,isbn ,author)

    assert book.title == title, f"Erwartet: {title} bekommen: {book.title}"
    assert book.isbn == isbn, f"Erwartet: {isbn} bekommen: {book.isbn}"
    assert book.author == author, f"Erwartet: {author} bekommen: {book.author}"
print("Test bestanden Book")
