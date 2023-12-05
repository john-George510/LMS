from django import forms
from .models import Student, Book

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

class BookRegistrationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'genre', 'publication_year', 'publisher', 'total_copies', 'available_copies']
