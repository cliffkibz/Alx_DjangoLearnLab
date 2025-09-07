from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for easy filtering
    list_filter = ('publication_year', 'author')
    
    # Add search functionality
    search_fields = ('title', 'author')
    
    # Order by title by default
    ordering = ('title',)
    
    # Items per page
    list_per_page = 20
