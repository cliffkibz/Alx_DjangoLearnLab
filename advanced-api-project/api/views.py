from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# BookListView: List all books (read-only, open to all users)
class BookListView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.AllowAny]

# BookDetailView: Retrieve a single book by ID (read-only, open to all users)
class BookDetailView(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.AllowAny]

# BookCreateView: Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]

# BookUpdateView: Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]

# BookDeleteView: Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]

# Each view uses DRF generic views for efficient CRUD operations.
# Permissions are set so only authenticated users can create, update, or delete books.
# List and detail views are open to all (read-only).
