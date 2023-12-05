# Library Management System API

## Overview

The Library Management System API is a Django web application designed to manage student registrations, book inventory, and book issuing within a library. The API provides various functionalities for user authentication, student registration, book management, and issuing/returning books.

## Functionalities

1. **User Authentication:**
   - Authenticate users for login.

2. **Student Registration:**
   - Register new students.

3. **Get Students:**
   - Retrieve a list of students.

4. **Add Book:**
   - Add new books to the system.

5. **Issue Book:**
   - Issue books to students.

6. **Get All Books:**
   - Retrieve a list of all books.

7. **Book Details (GET and DELETE):**
   - GET: Retrieve details of a specific book.
   - DELETE: Delete a specific book.

8. **Update Book:**
   - Update details of a specific book.

9. **Get All Book Issues:**
   - Retrieve a list of all book issues.

10. **Get Student Books:**
    - Retrieve a list of books issued to a specific student.

## Technologies Used

- **Backend:**
  - Django (Python web framework)
  - Django REST Framework for API development
  - Database (e.g., PostgreSQL, SQLite)

- **Authentication:**
  - Token-based authentication

## Getting Started

Follow these steps to set up and run the inventory management system locally.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/john-George510/LMS.git
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment:**

    On Windows:

    ```bash
    env\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source env/bin/activate
    ```

4. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Create a superuser (for the Django admin):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser to access the application.
