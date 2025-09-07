#!/usr/bin/env python
import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_all_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return Book.objects.none()


def list_all_books_in_library(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()



def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


if __name__ == "__main__":
    # Example usage
    print("=== Sample Queries ===")

    # Query all books by a specific author
    author_books = query_all_books_by_author("J.K. Rowling")
    print(f"Books by J.K. Rowling: {list(author_books)}")

    # List all books in a library
    library_books = list_all_books_in_library("Central Library")
    print(f"Books in Central Library: {list(library_books)}")

    # Retrieve librarian for a library
    librarian = retrieve_librarian_for_library("Central Library")
    print(f"Librarian for Central Library: {librarian}")