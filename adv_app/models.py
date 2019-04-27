from django.db import models
from django.urls import reverse
# Create your models here.

# Setup database fields

# School
#    - name
#    - principal
#    - location

# Student
#    - name
#    - age
#    - school (foreign key linking school and student - referencing primary key School)


# IF NO PRIMARY KEY IS SET, DJANGO WILL AUTOMATICALLY ASSIGN ID FOR EVERY ENTRY
class School(models.Model):
    name = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("adv_app:detail", kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(
        School, related_name="students", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
