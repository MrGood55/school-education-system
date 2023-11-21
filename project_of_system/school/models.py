from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.




class School(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    # Other school-related fields as needed


    def __str__(self):
        return self.name



class Person(AbstractUser):
    # Add your custom fields here, such as 'first_name', 'middle_name', 'last_name', 'email', 'school', and 'status'
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('teacher', 'Teacher'),
        ('special_staff', 'Special Staff'),
        ('administrator', 'Administrator'),
    ], default='student')
    nationality = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    # Other fields as needed

    def __str__(self):
        return f"{self.name} {self.surname} - {self.status}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    staff = models.ForeignKey(Person, on_delete=models.CASCADE)
    students = models.ManyToManyField(Person, related_name='enrolled_classes', limit_choices_to={'status': 'student'})
    subjects = models.ManyToManyField(Subject)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name

class Evaluation(models.Model):
    student = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='evaluations_as_student', limit_choices_to={'status': 'student'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    staff = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='evaluations_as_staff',
                               limit_choices_to={'status__in': ['teacher', 'special_staff', 'administrator']})
    # grade = models.DecimalField(max_digits=5, decimal_places=2,blank=True)
    grade = models.CharField(max_length=10,blank=True)
    date = models.DateField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True,auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.staff} - {self.grade} ({self.date})"
