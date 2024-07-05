from django.db import models

class University(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"