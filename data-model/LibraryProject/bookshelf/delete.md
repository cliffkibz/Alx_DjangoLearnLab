# Delete Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(f"Number of books in database: {all_books.count()}")
```

## Expected Output
```python
# Output:
# Number of books in database: 0
# The book has been successfully deleted from the database
```
