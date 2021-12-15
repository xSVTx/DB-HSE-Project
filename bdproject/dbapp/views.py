from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import *
from .models import *
from django.db import connections
from django.urls import reverse

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

#--------------------CoursesViews---------------------#

class coursesListView(ListView):
    template_name = 'courses/course_list.html'
    queryset = Courses.objects.all()


class coursesCreateView(CreateView):
    template_name = 'courses/course_create.html'
    form_class = CourseModelForm
    queryset = Courses.objects.all()


class coursesDetailView(DetailView):
    template_name = 'courses/course_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Courses, course_id=id_)


class coursesDeleteView(DeleteView):
    template_name = 'courses/course_list.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Courses, course_id=id_)

    def get_success_url(self):
        return reverse('dbapp:course-list')


def deleteCourse(request, id):
    temp = get_object_or_404(Courses, course_id=id)
    temp.delete()
    return redirect('/courses/')


class coursesUpdateView(UpdateView):
    template_name = 'courses/course_create.html'
    form_class = CourseModelForm

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Courses, course_id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dbapp:course-list')


def coursesAllDelete(request):
    Courses.objects.all().delete()
    return redirect('/courses/')

#----------------------ExamViews----------------------#

class examListView(ListView):
    template_name = 'exams/exam_list.html'
    queryset = Exams.objects.all()


class examCreateView(CreateView):
    template_name = 'exams/exam_create.html'
    form_class = ExamModelForm
    queryset = Exams.objects.all()


class examDetailView(DetailView):
    template_name = 'exams/exam_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Exams, exam_id=id_)


def deleteExam(request, id):
    temp = get_object_or_404(Exams, exam_id=id)
    temp.delete()
    return redirect('/exam/')


class examUpdateView(UpdateView):
    template_name = 'exams/exam_create.html'
    form_class = ExamModelForm

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Exams, exam_id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dbapp:exam-list')


def examAllDelete(request):
    Exams.objects.all().delete()
    return redirect('/exam/')
       

#---------------------LectureViews--------------------#

class lectureListView(ListView):
    template_name = 'lectures/lecture_list.html'
    queryset = Lectures.objects.all()


class lectureDetailView(DetailView):
    template_name = 'lectures/lecture_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Lectures, lecture_id=id_)


class lectureCreateView(CreateView):
    template_name = 'lectures/lecture_create.html'
    form_class = LectureModelForm
    queryset = Lectures.objects.all()


def deleteLecture(request, id):
    temp = get_object_or_404(Lectures, lecture_id=id)
    temp.delete()
    return redirect('/lecture/')


class lectureUpdateView(UpdateView):
    template_name = 'lectures/lecture_create.html'
    form_class = LectureModelForm

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Lectures, lecture_id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dbapp:lecture-list')


def lectureAllDelete(request):
    Lectures.objects.all().delete()
    return redirect('/lecture/')

#-------------------AssignmentViews-------------------#

class assignmentListView(ListView):
    template_name = 'assignments/assignment_list.html'
    queryset = Assignment.objects.all()


class assignmentDetailView(DetailView):
    template_name = 'assignments/assignment_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Assignment, assignment_id=id_)


class assignmentCreateView(CreateView):
    template_name = 'assignments/assignment_create.html'
    form_class = AssignmentModelForm
    queryset = Assignment.objects.all()


def deleteAssignment(request, id):
    temp = get_object_or_404(Assignment, assignment_id=id)
    temp.delete()
    return redirect('/assignment/')


class assignmentUpdateView(UpdateView):
    template_name = 'assignments/assignment_create.html'
    form_class = AssignmentModelForm

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Assignment, assignment_id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dbapp:assignment-list')


def assignmentAllDelete(request):
    Assignment.objects.all().delete()
    return redirect('/assignment/')

#---------------------MaterialViews-------------------#

class materialListView(ListView):
    template_name = 'materials/material_list.html'
    queryset = Materials.objects.all()


class materialDetailView(DetailView):
    template_name = 'materials/material_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Materials, material_id=id_)


class materialCreateView(CreateView):
    template_name = 'materials/material_create.html'
    form_class = MaterialModelForm
    queryset = Materials.objects.all()


def deleteMaterials(request, id):
    temp = get_object_or_404(Materials, material_id=id)
    temp.delete()
    return redirect('/materials/')


class materialUpdateView(UpdateView):
    template_name = 'materials/material_create.html'
    form_class = MaterialModelForm

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Materials, material_id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dbapp:material-list') 


def materialAllDelete(request):
    Materials.objects.all().delete()
    return redirect('/materials/')       

#---------------------MaterialViews-------------------#

class recordingListView(ListView):
    template_name = 'recordings/recording_list.html'
    queryset = Recordings.objects.all()


class recordingDetailView(DetailView):
    template_name = 'recordings/recording_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Recordings, recording_id=id_)


class recordingCreateView(CreateView):
    template_name = 'recordings/recording_create.html'
    form_class = RecordingModelForm
    queryset = Recordings.objects.all()

    def get_success_url(self):
        return reverse('dbapp:recording-list')


def deleteRecording(request, id):
    temp = get_object_or_404(Recordings, recording_id=id)
    temp.delete()
    return redirect('/recordings/')


class  recordingUpdateView(UpdateView):
    template_name = 'recordings/recording_create.html'
    form_class = RecordingModelForm

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Recordings,  recording_id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dbapp:recording-list') 


def recordingAllDelete(request):
    Recordings.objects.all().delete()
    return redirect('/recordings/') 

#---------------------TeacherViews--------------------#

class teacherListView(ListView):
    template_name = 'teacher/teacher_list.html'
    queryset = Teacher.objects.all()


class teacherDetailView(DetailView):
    template_name = 'teacher/teacher_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Teacher, teacher_id=id_)


class teacherCreateView(CreateView):
    template_name = 'teacher/teacher_create.html'
    form_class = TeacherModelForm
    queryset = Teacher.objects.all()


class teacherUpdateView(UpdateView):
    template_name = 'teacher/teacher_create.html'
    form_class = TeacherModelForm

    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Teacher, teacher_id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dbapp:teacher-list') 


def deleteTeacher(request, id):
    temp = get_object_or_404(Teacher, teacher_id=id)
    temp.delete()
    return redirect('/teacher/')


def teacherAllDelete(request):
    Teacher.objects.all().delete()
    return redirect('/teacher/')        