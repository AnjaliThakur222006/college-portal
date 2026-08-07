from django.db import models


# Student Model

class Student(models.Model):

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=30)

    email = models.EmailField(unique=True)

    enrollment_date = models.DateField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



# Course Model

class Course(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField()


    students = models.ManyToManyField(
        Student,
        through='Enrollment'
    )


    def __str__(self):
        return self.name



# Enrollment Model

class Enrollment(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )


    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )


    enrollment_date = models.DateField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.student} enrolled in {self.course}"


        