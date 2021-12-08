from django import forms

from .models import Teacher


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields =[
            'teacher_id',
            'teachercredentials',
            'teacherphonenumber',
            'teacheremail'
        ]