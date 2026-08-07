from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    course = models.CharField(max_length=100)

    def _str_(self):
        return self.name

