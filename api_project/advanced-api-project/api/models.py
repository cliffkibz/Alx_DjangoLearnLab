
from django.db import models

# Author model represents a book author with a name field.
class Author(models.Model):
	name = models.CharField(max_length=100, help_text="The author's full name.")

	def __str__(self):
		return self.name

# Book model represents a book with title, publication year, and a foreign key to Author.
class Book(models.Model):
	title = models.CharField(max_length=200, help_text="The title of the book.")
	publication_year = models.IntegerField(help_text="Year the book was published.")
	author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text="The author of the book.")

	def __str__(self):
		return f"{self.title} ({self.publication_year})"

	# The Author-Book relationship is one-to-many: one Author can have many Books (via ForeignKey).
