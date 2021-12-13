from django.urls import path
from .views import *

app_name = 'dbapp'
urlpatterns = [
    path('teacher/', teacherListView.as_view(), name='teacher-list'),
    path('teacher/<int:id>/', teacherDetailView.as_view(), name='teacher-detail'),
    path('teacher/create/', teacherCreateView.as_view(), name='teacher-create'),
    path('teacher/<int:id>/update/', teacherUpdateView.as_view(), name='teacher-update'),
    path('teacher/<int:id>/delete/', teacherDeleteView.as_view(), name='teacher-delete'),
    path('teacher/delete/', teacherAllDelete),
    
    path('courses/', coursesListView.as_view(), name='course-list'),
    path('courses/<int:id>/', coursesDetailView.as_view(), name='course-detail'),
    path('courses/create/', coursesCreateView.as_view(), name='course-create'),
    path('courses/<int:id>/update/', coursesUpdateView.as_view(), name='course-update'),
    path('courses/<int:id>/delete/', coursesDeleteView.as_view(), name='course-delete'),
    path('courses/delete/', coursesAllDelete),

    path('exam/', examListView.as_view(), name='exam-list'),
    path('exam/<int:id>/', examDetailView.as_view(), name='exam-detail'),
    path('exam/create/', examCreateView.as_view(), name='exam-create'),
    path('exam/<int:id>/update/', examUpdateView.as_view(), name='exam-update'),
    path('exam/<int:id>/delete/', examDeleteView.as_view(), name='exam-delete'),
    path('exam/delete/', examAllDelete),

    path('lecture/', lectureListView.as_view(), name='lecture-list'),
    path('lecture/<int:id>/', lectureDetailView.as_view(), name='lecture-detail'),
    path('lecture/create/', lectureCreateView.as_view(), name='lecture-create'),
    path('lecture/<int:id>/update/', lectureUpdateView.as_view(), name='lecture-update'),
    path('lecture/<int:id>/delete/', lectureDeleteView.as_view(), name='lecture-delete'),
    path('lecture/delete/', lectureAllDelete),

    path('assignment/', assignmentListView.as_view(), name='assignment-list'),
    path('assignment/<int:id>/', assignmentDetailView.as_view(), name='assignment-detail'),
    path('assignment/create/', assignmentCreateView.as_view(), name='assignment-create'),
    path('assignment/<int:id>/update/', assignmentUpdateView.as_view(), name='assignment-update'),
    path('assignment/<int:id>/delete/', assignmentDeleteView.as_view(), name='assignment-delete'),
    path('assignment/delete/', assignmentAllDelete),

    path('materials/', materialListView.as_view(), name='material-list'),
    path('materials/<int:id>/', materialDetailView.as_view(), name='material-detail'),
    path('materials/create/', materialCreateView.as_view(), name='material-create'),
    path('materials/<int:id>/update/', materialUpdateView.as_view(), name='material-update'),
    path('materials/<int:id>/delete/', materialDeleteView.as_view(), name='material-delete'),
    path('materials/delete/', materialAllDelete),

    path('recordings/', recordingListView.as_view(), name='recording-list'),
    path('recordings/<int:id>/', recordingDetailView.as_view(), name='recording-detail'),
    path('recordings/create/', recordingCreateView.as_view(), name='recording-create'),
    path('recordings/<int:id>/update/', recordingUpdateView.as_view(), name='recording-update'),
    path('recordings/<int:id>/delete/', recordingDeleteView.as_view(), name='recording-delete'),
    path('recordings/delete/', recordingAllDelete),

]
