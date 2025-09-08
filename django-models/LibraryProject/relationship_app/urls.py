from django.urls import path
from .views import list_books
from . import views
from django.contrib.auth import views as auth_views
from .views import register
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # or wherever you want
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

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
