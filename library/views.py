from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Book, BookIssue
from .forms import StudentRegistrationForm, BookRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .serializers import BookSerializer, BookIssueSerializer

@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success':True, 'message' : 'Login succesful', 'username' : username})
        else:
            return JsonResponse({'success':False, 'message' : 'Invalid credentials'}, status=401)

@csrf_exempt 
def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            return JsonResponse({'success': True, 'message': 'Student registered successfully', 'student_id': new_student.id})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        form = BookRegistrationForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            return JsonResponse({'success': True, 'message': 'Book added successfully', 'book_id': new_book.id})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

@login_required
@csrf_exempt
def issue_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        student_id = request.POST.get('student_id')
        issue_date = request.POST.get('issue_date')
        due_date = request.POST.get('due_date')
        print(request.body)
        print(request.POST)
        try:
            book = Book.objects.get(id=book_id)
            student = Student.objects.get(id=student_id)
            if book.available_copies == 0:
                return JsonResponse({'success': False, 'message': 'No available copies'}, status=400)
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Book does not exist'}, status=404)
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Student does not exist'}, status=404)

        book_issue = BookIssue(book=book, student=student, issue_date=issue_date, due_date=due_date)
        book_issue.save()
        book.available_copies -= 1
        return JsonResponse({'success': True, 'message': 'Book issued successfully', 'book_issue_id': book_issue.id})

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

def get_all_books(request):
    books = Book.objects.all()
    serialized_books = BookSerializer(books, many=True)
    return JsonResponse({'success': True, 'books': serialized_books.data})

@login_required
@csrf_exempt
def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        if request.method == 'POST':
            for field,value in request.POST.items():
                if hasattr(book, field):
                    setattr(book, field, value)
            book.save()
            return JsonResponse({'success': True, 'message': 'Book updated successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)
    except Book.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Book does not exist'}, status=404)

@login_required 
def book(request, book_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=book_id)
            serializer_book = BookSerializer(book)
            return JsonResponse({'success': True, 'book': serializer_book.data})
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Book does not exist'}, status=404)
    elif request.method == 'DELETE':
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return JsonResponse({'success': True, 'message': 'Book deleted successfully'})
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Book does not exist'}, status=404)

def get_student_books(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        book_issues = BookIssue.objects.filter(student=student)
        serialized_book_issues = BookIssueSerializer(book_issues, many=True)
        return JsonResponse({'success': True, 'book_issues': serialized_book_issues.data})
    except Student.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Student does not exist'}, status=404)
    
def get_all_book_issues(request):
    book_issues = BookIssue.objects.all()
    serialized_book_issues = BookIssueSerializer(book_issues, many=True)
    return JsonResponse({'success': True, 'book_issues': serialized_book_issues.data})