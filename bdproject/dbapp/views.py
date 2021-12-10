from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import TeacherModelForm
from .models import Teacher
from django.urls import reverse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})


def courses_view(request, *args, **kwargs):
    return render(request, "courses.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


class testListView(ListView):
    template_name = 'teacher/teacher_list.html'
    queryset = Teacher.objects.all()


class testDetailView(DetailView):
    template_name = 'teacher/teacher_detail.html'
    # queryset = Teacher.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id") # Had to be 'teacher_id', but doesnt work for some reason
        return get_object_or_404(Teacher, teacher_id=id_)


class testCreateView(CreateView):
    template_name = 'teacher/teacher_create.html'
    form_class = TeacherModelForm
    queryset = Teacher.objects.all()


class testUpdateView(UpdateView):
    template_name = 'teacher/teacher_create.html'
    form_class = TeacherModelForm

    def get_object(self):
        id_ = self.kwargs.get("id") # Had to be 'teacher_id', but doesnt work for some reason
        return get_object_or_404(Teacher, teacher_id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dbapp:teacher-list') 


class testDeleteView(DeleteView):
    template_name = 'teacher/teacher_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Teacher, teacher_id=id_)

    def get_success_url(self):
        return reverse('dbapp:teacher-list')