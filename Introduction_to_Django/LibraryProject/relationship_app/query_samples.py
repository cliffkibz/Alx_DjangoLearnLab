#!/usr/bin/env python
import os
import sys
import django

# Ensure the project root (containing manage.py and LibraryProject/) is on sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, '..'))  # .../LibraryProject
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library


def query_samples():
    print("=== Sample Queries ===")

    # Query 1: All books by a specific author
    print("\n1. Query all books by a specific author:")
    try:
        author = Author.objects.first()  # Get first author for example
        if author:
            books_by_author = author.books.all()
            print(f"Books by {author.name}:")
            for book in books_by_author:
                print(f"  - {book.title}")
        else:
            print("No authors found in database.")
    except Exception as e:
        print(f"Error querying books by author: {e}")

    # Query 2: List all books in a library
    print("\n2. List all books in a library:")
    try:
        library = Library.objects.first()  # Get first library for example
        if library:
            books_in_library = library.books.all()
            print(f"Books in {library.name} library:")
            for book in books_in_library:
                print(f"  - {book.title}")
        else:
            print("No libraries found in database.")
    except Exception as e:
        print(f"Error querying books in library: {e}")

    # Query 3: Retrieve the librarian for a library
    print("\n3. Retrieve the librarian for a library:")
    try:
        library = Library.objects.first()  # Get first library for example
        if library and hasattr(library, 'librarian'):
            librarian = library.librarian
            print(f"Librarian for {library.name}: {librarian.name}")
        else:
            print("No librarian found for this library.")
    except Exception as e:
        print(f"Error querying librarian: {e}")


if __name__ == "__main__":
    query_samples()
