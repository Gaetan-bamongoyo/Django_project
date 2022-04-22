from django.db import models

# Create your models here.
class Poste(models.Model):
    posteId = models.AutoField(primary_key=True)
    posteDesignation = models.CharField(max_length=100)
    
class Employee(models.Model):
    employeId = models.AutoField(primary_key=True)
    employeNom = models.CharField(max_length=100)
    employePostnom = models.CharField(max_length=100)
    employeSexe = models.CharField(max_length=100)
    employeAdress = models.TextField()
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE)
    
    
