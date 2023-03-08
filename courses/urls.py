from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses-list')
]
