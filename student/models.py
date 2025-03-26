from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 50, verbose_name="Student Name")
    roll = models.IntegerField(unique=True, verbose_name="Roll Number")
    father_name = models.CharField(max_length = 50, blank = True, null = True, verbose_name="Father Name")

    def __str__(self):
        return f"{self.name},{self.roll},{self.father_name}"
