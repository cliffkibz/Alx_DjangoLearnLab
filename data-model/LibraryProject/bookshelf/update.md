# Update Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
```

## Expected Output
```python
# Output:
# Updated title: Nineteen Eighty-Four
# The book title has been successfully updated in the database
```
