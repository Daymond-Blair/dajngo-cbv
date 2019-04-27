from django.contrib import admin
from adv_app.models import School, Student
# Register your models here.

# Allow creation of School and Student fields through admin.
admin.site.register(School)
admin.site.register(Student)
