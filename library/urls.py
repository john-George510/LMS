from django.urls import path
from .views import admin_login, register_student, add_book, issue_book, get_all_books,book, update_book, get_all_book_issues, get_student_books

urlpatterns = [
    path('login/', admin_login, name='login'),
    path('register/', register_student, name='register_student'),
    path('add_book/', add_book, name='add_book'),
    path('issue_book/', issue_book, name='issue_book'),
    path('get_books/', get_all_books, name='get_books'),
    path('book/<int:book_id>/', book, name='book'),
    path('book/<int:book_id>/update/', update_book, name='update_book'),
    path('get_book_issues/', get_all_book_issues, name='get_book_issues'),
    path('get_student_books/', get_student_books, name='get_student_books'),
]
