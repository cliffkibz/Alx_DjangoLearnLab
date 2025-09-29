<<<<<<< HEAD
"""
See 'auth_permissions_doc.md' in this directory for details on authentication and permissions setup.
"""

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can access this viewset
    permission_classes = [permissions.IsAuthenticated]

    # You can use IsAdminUser or custom permissions for more control
    # Example: permission_classes = [permissions.IsAdminUser]
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 146de713437321d0f343a53201206dd113c6ee78
