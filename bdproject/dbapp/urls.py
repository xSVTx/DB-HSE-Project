from django.urls import path
from .views import (
    testListView,
    testDetailView,
    testCreateView,
    testUpdateView,
    testDeleteView
)

app_name = 'dbapp'
urlpatterns = [
    path('', testListView.as_view(), name='teacher-list'),
    path('<int:id>/', testDetailView.as_view(), name='teacher-detail'),
    path('create/', testCreateView.as_view(), name='teacher-create'),
    path('<int:id>/update', testUpdateView.as_view(), name='teacher-update'),
    path('<int:id>/delete/', testDeleteView.as_view(), name='teacher-delete')
]
