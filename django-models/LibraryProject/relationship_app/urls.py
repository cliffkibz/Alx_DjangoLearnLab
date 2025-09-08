from django.urls import path
from .views import list_books
from . import views

urlpatterns = [
    path('books/', views.list_books, name='relationship_app/list_books'),   # FBV
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='relationship_app/library_detail'),  # CBV
]
