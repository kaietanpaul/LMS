from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from . import models
from .permissions import OwnerRequiredMixin


class CourseListView(ListView):
    model = models.Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'courses/course_details.html'
    context_object_name = 'course'


class CourseDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = models.Course
    success_url = reverse_lazy('courses:courses-list')
    login_url = reverse_lazy('users:login')
    template_name = 'courses/course-delete.html'
    context_object_name = 'course'


class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Course
    fields = ('title', 'slug', 'subject', 'overview', 'course_image')
    template_name = 'courses/course_create.html'
    success_url = reverse_lazy('courses:courses-list')
    login_url = reverse_lazy('users:login')
    permission_required = 'courses.add_course'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

