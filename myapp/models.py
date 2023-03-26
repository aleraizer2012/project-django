from django.db import models

# Create your models here.
class DocNumber(models.Model):
    doctype = models.CharField(max_length=50)
    year = models.IntegerField()
    number = models.IntegerField()
    subject = models.CharField(max_length=200)
    recipient = models.CharField(max_length=100)
    departmentrecipient = models.CharField(max_length=100)