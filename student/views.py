from django.shortcuts import render


def home(request):
    return render(request, 'student/index.html')


def student(request):
    student=Student.object.all()
    return render(request, 'student/index.html')