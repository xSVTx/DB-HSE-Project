from django.contrib import admin
from .models import Teacher, Assignment, Exams, Recordings, Materials, Lectures, Courses

admin.site.register(Teacher)
admin.site.register(Materials)
admin.site.register(Assignment)
admin.site.register(Exams)
admin.site.register(Recordings)
admin.site.register(Lectures)
admin.site.register(Courses)
# admin.site.register(LecturesAssignement)
# admin.site.register(CoursesTeacher)