# LibraryProject

This is a Django project created for learning purposes.  
It includes the basic Django setup with `manage.py`, `settings.py`, and `urls.py`.

## Project Structure

```
LibraryProject/
├── manage.py              # Django's command-line utility
├── README.md              # This file
├── db.sqlite3             # SQLite database file
├── __init__.py            # Python package marker
├── settings.py            # Django settings
├── urls.py               # URL configuration
├── wsgi.py               # WSGI application entry point
└── asgi.py               # ASGI application entry point
```

## Setup Instructions

1. **Install Django** (if not already installed):
   ```bash
   pip install django
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

4. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Features

- Basic Django project structure
- SQLite database configuration
- Development server ready
- Admin interface available at `/admin/`

## Development

This project is set up for development with:
- DEBUG = True
- SQLite database
- Static files configuration
- Basic middleware stack

## Next Steps

- Create Django apps for specific functionality
- Define models for your data
- Create views and templates
- Configure URL patterns
