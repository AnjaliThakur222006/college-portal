from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm


# ==========================
# HOME PAGE
# ==========================

def home(request):

    data = {
        'name': 'Anjali',
        'course': 'WDP',
        'college': 'JG-University'
    }

    subject = ['python', 'Agile', 'BigData']

    students = Student.objects.all()

    return render(request,'index.html',{
        'data':data,
        'subject_List':subject,
        'students':students
    })



# ==========================
# ABOUT
# ==========================

def about(request):

    return render(request,'about.html')



# ==========================
# CONTACT
# ==========================

def contact(request):

    return render(request,'contact.html')



# ==================================================
# STUDENT CRUD
# ==================================================


# READ ALL STUDENT

def student(request):

    students = Student.objects.all()

    return render(request,'student.html',{
        'students':students
    })



# VIEW SINGLE STUDENT

def view_student(request,id):

    student = get_object_or_404(Student,id=id)

    return render(request,'view_student.html',{
        'student':student
    })


# ==================================================
# ADD STUDENT (Old Method - Commented)
# ==================================================

"""
def add_student(request):

    if request.method == "POST":

        Student.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            enrollment_date=request.POST['enrollment_date']
        )

        return redirect('/student/')

    return render(request, 'add_student.html')
"""

# ==================================================
# ADD STUDENT USING DJANGO MODEL FORM
# ==================================================

def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/student/')

    else:

        form = StudentForm()

    return render(request, 'add_student.html', {
        'form': form
    })









# UP
# 
# 
# 
# 
# 
# 
# 
# 
# DATE STUDENT

def update_student(request,id):

    student = get_object_or_404(Student,id=id)


    if request.method == "POST":

        student.first_name = request.POST['first_name']

        student.last_name = request.POST['last_name']

        student.email = request.POST['email']

        student.enrollment_date = request.POST['enrollment_date']


        student.save()


        return redirect('/student/')


    return render(request,'update_student.html',{
        'student':student
    })



# DELETE STUDENT

def delete_student(request,id):

    student = get_object_or_404(Student,id=id)

    student.delete()

    return redirect('/student/')



# ==================================================
# COURSE CRUD
# ==================================================


# READ COURSE

def course(request):

    courses = Course.objects.all()

    return render(request,'course.html',{
        'courses':courses
    })



# ADD COURSE

def add_course(request):

    if request.method == "POST":

        Course.objects.create(

            name=request.POST['name'],

            description=request.POST['description'],

            start_date=request.POST['start_date'],

            end_date=request.POST['end_date']

        )


        return redirect('/course/')


    return render(request,'add_course.html')



# UPDATE COURSE

def update_course(request,id):

    course = get_object_or_404(Course,id=id)


    if request.method == "POST":

        course.name = request.POST['name']

        course.description = request.POST['description']

        course.start_date = request.POST['start_date']

        course.end_date = request.POST['end_date']


        course.save()


        return redirect('/course/')


    return render(request,'update_course.html',{
        'course':course
    })



# DELETE COURSE

def delete_course(request,id):

    course = get_object_or_404(Course,id=id)

    course.delete()

    return redirect('/course/')

    