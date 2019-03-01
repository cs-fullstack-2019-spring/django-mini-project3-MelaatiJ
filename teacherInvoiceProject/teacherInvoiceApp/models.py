from django.db import models
from django.utils.timezone import now


# Create your models here.


class TeacherModel(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_school = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    date_worked = models.DateField()
    date_of_entry = models.DateTimeField(default=now)

    def __str__(self):
        return self.teacher_name, self.teacher_school
