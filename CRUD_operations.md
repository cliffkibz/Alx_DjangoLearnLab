# CRUD Operations for Book Model

This document contains all the CRUD (Create, Read, Update, Delete) operations performed on the Book model in the Django shell.

## 1. Create Operation

### Command
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

### Expected Output
```python
# Output: <Book: 1984 by George Orwell (1949)>
# The book is now saved in the database
```

## 2. Retrieve Operation

### Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

### Expected Output
```python
# Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
```

## 3. Update Operation

### Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
```

### Expected Output
```python
# Output:
# Updated title: Nineteen Eighty-Four
# The book title has been successfully updated in the database
```

## 4. Delete Operation

### Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(f"Number of books in database: {all_books.count()}")
```

### Expected Output
```python
# Output:
# Number of books in database: 0
# The book has been successfully deleted from the database
```

## Summary

All CRUD operations have been successfully implemented and tested:
- ✅ **Create**: Book instance created with title "1984", author "George Orwell", publication year 1949
- ✅ **Read**: Book retrieved and all attributes displayed
- ✅ **Update**: Book title updated from "1984" to "Nineteen Eighty-Four"
- ✅ **Delete**: Book deleted and deletion confirmed by checking database count
