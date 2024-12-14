from django.db import models

class Reg(models.Model):
    optn=[['male','MALE'],['female','FEMALE'],['others','OTHERS']]
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    gender=models.CharField(max_length=20,choices=optn)
    
