from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=100)
    # Other school-related fields as needed

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    role = models.CharField(max_length=50)  # e.g., Principal, Administrator, etc.
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.role}"

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # Other student-related fields as needed

    def __str__(self):
        return f"{self.name} {self.surname}"

class Parent(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    # Other parent-related fields as needed

    def __str__(self):
        return f"{self.name} {self.surname}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # Other subject-related fields as needed

    def __str__(self):
        return self.name

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    subjects = models.ManyToManyField(Subject)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    # Other class-related fields as needed

    def __str__(self):
        return self.class_name

class Evaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    # Other evaluation-related fields as needed

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.staff} - {self.grade} ({self.date})"


