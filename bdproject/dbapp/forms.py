from django import forms
from django.forms import widgets

from .models import *


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields =[
            'teacher_id',
            'teacherfullname',
            'teachertel',
            'teachermail',
            'exam',
            'courses'
        ]
        labels ={
            'teacher_id': '__ID__',
            'teachercredentials': 'Name',
            'teacherphonenumber': 'PhNu',
            'teacheremail': 'mail',
            'courses': 'cour'
        }
        widgets ={
            'teacher_id': widgets.Textarea(attrs={'cols': 20, 'rows': 1}),
        }


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields =[
            'course_id',
            'coursename',
            'coursestartdate',
            'courseenddate',
        ]
        labels ={
            'course_id': '__ID__',
            'coursename': 'Name',
            'coursestartdate': 'StartDate',
            'courseenddate': 'EndDate',
        }


class ExamModelForm(forms.ModelForm):
    class Meta:
        model = Exams
        fields =[
            'exam_id',
            'examdate',
            'examtimestart',
            'examtimeend',
            'course'
        ]
        labels ={
            'exam_id': '__ID__',
            'examdate': 'Date',
            'examtimestart': 'startTime',
            'examtimeend': 'endTime'
        }


class LectureModelForm(forms.ModelForm):
    class Meta:
        model = Lectures
        fields =[
            'lecture_id',
            'lecturesname',
            'lectureformat',
            'lecturedate',
            'lecturetimestart',
            'lecturetimeend',
            'course',
            'recording'
        ]


class AssignmentModelForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields =[
            'assignment_id',
            'assignmentinfo',
            'assignmentdeadline',
            'assignmentstatus',
            'lectures'
        ]



class MaterialModelForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields =[
            'material_id',
            'materialinfo',
            'materiallink',
            'course'
        ]


class RecordingModelForm(forms.ModelForm):
    class Meta:
        model = Recordings
        fields =[
            'recording_id',
            'recordingURL',
            'lecture'
        ]        