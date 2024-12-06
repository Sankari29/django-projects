from django.db import models
class s_table(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=3)
    mob=models.CharField(max_length=10)
    clas=models.CharField(max_length=10)


