from django.contrib import admin
from .models import Teacher, Assignment, Exams, Recordings, Materials, LecturesAssignement, Lectures, CoursesTeacher, Courses

admin.site.register(Teacher)
admin.site.register(Materials)
admin.site.register(Assignment)
admin.site.register(Exams)
admin.site.register(Recordings)
admin.site.register(Lectures)
admin.site.register(LecturesAssignement)
admin.site.register(CoursesTeacher)
admin.site.register(Courses)