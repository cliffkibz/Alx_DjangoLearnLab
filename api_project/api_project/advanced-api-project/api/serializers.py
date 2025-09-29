from rest_framework import serializers
from .models import Author, Book

# BookSerializer serializes all fields of the Book model and validates publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not in the future.
        """
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future.')
        return value

# AuthorSerializer serializes the name and includes a nested list of books using BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True, source='book_set')

    class Meta:
        model = Author
        fields = ['name', 'books']

    # The relationship between Author and Book is handled by the ForeignKey in Book
    # and the nested BookSerializer here, which serializes all books for each author.
