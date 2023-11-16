from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField()
    second_name = models.CharField()
    third_name = models.CharField()
    email = models.EmailField()

    group = models.ForeignKey()
    school = models.ForeignKey()
    
class Personal(models.Model):
    name = models.CharField()
    second_name = models.CharField()
    third_name = models.CharField()
    email = models.EmailField()
    position = models.CharField()

    school = models.ForeignKey()


class Subject(models.Model):
    title = models.CharField()


