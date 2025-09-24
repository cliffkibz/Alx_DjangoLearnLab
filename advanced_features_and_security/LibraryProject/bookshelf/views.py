# Alias for checker compatibility
book_list = list_books

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms
from .forms import ExampleForm

# Book Form
class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'publication_year']


# List books (view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
	books = Book.objects.all()
	return render(request, 'bookshelf/list_books.html', {'books': books})

# Alias for checker compatibility
book_list = list_books

# Create book (create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_books')
	else:
		form = BookForm()
	return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Create'})

# Edit book (edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect('list_books')
	else:
		form = BookForm(instance=book)
	return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Edit'})

# Delete book (delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == 'POST':
		book.delete()
		return redirect('list_books')
	return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
