from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
<<<<<<< HEAD
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update-pk'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete-pk'),
=======
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
>>>>>>> 146de713437321d0f343a53201206dd113c6ee78
]
