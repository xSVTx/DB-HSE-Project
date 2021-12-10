from django import forms

from .models import Teacher


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields =[
            'teacher_id',
            'teachercredentials',
            'teacherphonenumber',
            'teacheremail',
            'exam'
        ]
        widgets = {'teacher_id': forms.NumberInput(attrs={ 'class': 'form-control' }), 
            'teachercredentials': forms.TextInput(attrs={ 'class': 'form-control' }),
            'teacheremail': forms.EmailInput(attrs={'class': 'form-control' }),
            'exam': forms.Select()
        }