# Ethara Project - Role-Based Task Management Application

A full-stack role-based task management web application built with Django and Django REST Framework. The application provides robust project and task management features, incorporating strict role-based access control, secure API authentication, and a responsive frontend with a modern UI (including dark mode). It is designed to be production-ready and easily deployable to platforms like Railway.

## Features

- **User Authentication & Authorization**: Secure login and registration using JWT (JSON Web Tokens).
- **Role-Based Access Control**: Strict visibility and assignment logic. Administrative control over project members and task deletions.
- **Project Management**: Create, view, and manage projects. Admins can assign members to projects.
- **Task Management**: Create tasks within projects, assign them to specific members, and track their progress.
- **RESTful API**: Comprehensive API endpoints for Users, Projects, Tasks, and Authentication.
- **Modern UI**: Intuitive and responsive frontend powered by Django Templates, featuring modern aesthetics like dark mode and improved navigation.
- **Production Ready**: Configured with WhiteNoise for serving static files, Gunicorn as the WSGI HTTP Server, and dj-database-url for seamless database configuration.

## Tech Stack

- **Backend**: Django 6.x, Django REST Framework
- **Authentication**: SimpleJWT
- **Frontend**: Django Templates, HTML, CSS (Vanilla/Tailwind), JavaScript
- **Database**: SQLite (Local) / PostgreSQL (Production, via dj-database-url)
- **Deployment**: Configured for Railway (Procfile, runtime.txt, WhiteNoise)

## Prerequisites

- Python 3.10+
- pip (Python package installer)
- virtualenv (recommended)

## Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (Admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Frontend: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## API Endpoints Overview

- **Auth**: `/api/token/` (Login/Obtain Token), `/api/token/refresh/`
- **Users**: `/api/users/`
- **Projects**: `/api/projects/`
- **Tasks**: `/api/tasks/`

## Deployment

This project is configured for easy deployment on Railway:
1. Create a new project on Railway and connect your GitHub repository.
2. Railway will automatically detect the `Procfile` and `requirements.txt`.
3. Set your environment variables in the Railway dashboard:
   - `SECRET_KEY`: A secure random string
   - `DEBUG`: `False`
   - `DATABASE_URL`: Add a PostgreSQL database plugin in Railway and it will automatically populate this.
   - `ALLOWED_HOSTS`: Your Railway app domain.

## License

This project is licensed under the MIT License.
