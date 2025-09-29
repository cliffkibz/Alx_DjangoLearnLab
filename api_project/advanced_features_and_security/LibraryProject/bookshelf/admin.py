from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin


# Register CustomUser with custom admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = UserAdmin.list_display + ('date_of_birth',)

admin.site.register(CustomUser, CustomUserAdmin)

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
