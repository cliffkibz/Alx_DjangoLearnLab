# Introduction to Django - LibraryProject

## Project Overview
This is a Django project created for learning purposes as part of the Django development environment setup. The project serves as the foundation for developing Django applications and demonstrates the basic Django project structure.

## Project Structure
```
LibraryProject/
├── LibraryProject/          # Main project directory
│   ├── __init__.py         # Python package marker
│   ├── settings.py         # Django project settings
│   ├── urls.py             # URL declarations for the project
│   ├── wsgi.py             # WSGI application entry point
│   └── asgi.py             # ASGI application entry point
├── manage.py               # Django command-line utility
├── db.sqlite3              # SQLite database file
└── README.md               # This file
```

## Key Components

### settings.py
- Configuration file for the Django project
- Contains database settings, installed apps, middleware, and other project configurations
- Defines the project's behavior and environment

### urls.py
- The URL declarations for the project
- Acts as a "table of contents" of your Django-powered site
- Maps URL patterns to views

### manage.py
- A command-line utility that lets you interact with this Django project
- Used for running the development server, creating migrations, and other Django commands

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system
- pip (Python package installer)

### Installation Steps

1. **Install Django**
   ```bash
   pip install django
   ```

2. **Navigate to the project directory**
   ```bash
   cd LibraryProject
   ```

3. **Run the development server**
   ```bash
   python manage.py runserver
   ```

4. **Access the application**
   - Open a web browser
   - Go to http://127.0.0.1:8000/
   - You should see the default Django welcome page

## Development Server
The development server runs on http://127.0.0.1:8000/ by default. This server is for development purposes only and should not be used in production.

## Django Version
This project uses Django 5.2.5

## Repository Information
- **GitHub Repository**: Alx_DjangoLearnLab
- **Directory**: Introduction_to_Django
- **Author**: cliffkibz

## Next Steps
This project provides the basic foundation for Django development. Future enhancements may include:
- Creating Django apps
- Setting up models and databases
- Implementing views and templates
- Adding authentication and user management
- Building a complete library management system

## Contributing
This is a learning project. Feel free to explore and experiment with the Django framework.
