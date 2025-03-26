from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .import models

def profile(request):
    print(request.GET.get('name'))

    user_data = {
        'name': 'Muntaha',
        'nickname': 'Sidrat',  # Fixed typo
        'age': 21,
        'subjects': ['Math', 'Science', 'English'],
        'DOB': datetime(2003, 3, 8),
    }

    marks = [
        {"id": 1, "subject": "Math", "marks": 80},
        {"id": 2, "subject": "Science", "marks": 90},
        {"id": 3, "subject": "English", "marks": 85}
    ]

    student_data = models.Student.objects.all()
    print(student_data)

    # ✅ Merge all data into one dictionary before passing it to render
    context = {
        'user': user_data,
        'marks': marks,
        'student_data': student_data  # Fix: now included properly
    }

    return render(request, 'student/index.html', context)

def home(request):
    return HttpResponse("Welcome to my website")

def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return HttpResponse("Student deleted successfully")