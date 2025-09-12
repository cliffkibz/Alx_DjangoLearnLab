from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library   # 👈 this line must be here
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Role checks

def _has_role(user, expected):
    try:
        return hasattr(user, 'userprofile') and user.userprofile.role == expected
    except Exception:
        return False


def is_admin(user):
    return _has_role(user, 'Admin')


def is_librarian(user):
    return _has_role(user, 'Librarian')


def is_member(user):
    return _has_role(user, 'Member')


# Role-based views
@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member, login_url='login')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
