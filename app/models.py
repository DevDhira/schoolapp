from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=500)
    std = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    resulter = models.BooleanField(default=False)
    id_photo = models.FileField(upload_to='id_photo/')


    def __str__(self):
        return self.name
