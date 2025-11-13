from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course']
        )
        return redirect('/')
    return render(request, 'add.html')

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('/')
    return render(request, 'edit.html', {'student': student})

def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('/')
