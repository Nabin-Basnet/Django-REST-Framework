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

class Employee(models.Model):
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=200)
    job=models.CharField(max_length=50)


class teacher(models.Model):
    name=models.CharField(max_length=50)
    school=models.CharField(max_length=200)
    subject=models.CharField(max_length=50)


class staff(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    organization_name=models.CharField(max_length=100)
    work=models.CharField(max_length=100)

class Address(models.Model):
    add_num=models.CharField(max_length=20,default="add001")
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    country=models.CharField(max_length=50)