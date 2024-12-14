from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=7)
    mob=models.CharField(max_length=10)
    address=models.CharField(max_length=30)

class Signup(Profile):
    user=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    c_password=models.CharField(max_length=15)


# abstract class (model inheritance one of the type)
class common_info(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    class Meta:
        abstract=True
class Student(common_info):
    school=models.CharField(max_length=20)

class Teacher(common_info):
    subject=models.CharField(max_length=20)
