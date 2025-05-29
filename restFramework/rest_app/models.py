from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone_no=models.CharField(max_length=10)
    country=models.CharField(max_length=20)


class student(models.Model):
    std_name=models.CharField(max_length=50)
    std_id=models.IntegerField()
    std_address=models.CharField(max_length=50)

class teacher(models.Model):
    name=models.CharField(max_length=50)
    school=models.CharField(max_length=200)
    subject=models.CharField(max_length=50)