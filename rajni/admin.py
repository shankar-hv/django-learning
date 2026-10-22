from django.contrib import admin
from .models import Student, Teacher

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','marks']
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject']
    
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
