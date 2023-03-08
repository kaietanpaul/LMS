from django.shortcuts import render
from django.views.generic import ListView
from . import models


class CourseListView(ListView):
    model = models.Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'
