from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.
def home(request):
    students = Student.objects.all()
    
    context = {
        'students' : students
    }
    
    return render(request, 'home.html',context)

def student(request,id):
    student = Student.objects.get(id=id)
    
    context = {
        'student' : student,
    }
    return render(request, 'student.html',context)

def teachers(request):
    teachers = Teacher.objects.all()
    
    context = {
        'teachers' : teachers,
    }
    return render(request, 'teacher.html', context)