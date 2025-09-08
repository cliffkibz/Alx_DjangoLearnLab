from django.urls import path
from .views import list_books
from . import views
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]

urlpatterns = [
    path('books/', views.list_books, name='relationship_app/list_books'),   # FBV
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='relationship_app/library_detail'),  # CBV
]
