from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    author = Author.objects.get(name="John Doe")
    books_by_author = author.books.all()
    print("Books by John Doe:", [book.title for book in books_by_author])

    # List all books in a library
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
    print("Books in Central Library:", [book.title for book in books_in_library])

    # Retrieve the librarian for a library
    librarian = library.librarian
    print("Librarian of Central Library:", librarian.name)
