from django.urls import path
from .views import admin_login, register_student, add_book, issue_book, get_all_books,get_book

urlpatterns = [
    path('login/', admin_login, name='login'),
    path('register/', register_student, name='register_student'),
    path('add_book/', add_book, name='add_book'),
    path('issue_book/', issue_book, name='issue_book'),
    path('get_books/', get_all_books, name='get_books'),
    path('get_book/<int:book_id>/', get_book, name='get_book'),
]
