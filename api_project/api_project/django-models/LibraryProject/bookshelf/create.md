# Create Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Expected Output
```python
# The command will create a Book instance and return it
# Output: <Book: 1984 by George Orwell (1949)>
# The book is now saved in the database
```
