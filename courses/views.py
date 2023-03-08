from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
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


class CourseUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = models.Course
    fields = ('title', 'slug', 'subject', 'overview')
    template_name = 'courses/course-update.html'
    login_url = reverse_lazy('users:login')
    context_object_name = 'course'

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('courses:course-detail', kwargs={'pk': pk})


@login_required
def student_enrollment(request, course_slug):
    if request.method == 'POST':
        try:
            course = models.Course.objects.get(slug=course_slug)
            if course is not None:
                students = course.students.all()
                if request.user not in students:
                    course.students.add(request.user)
                    messages.add_message(request, messages.SUCCESS, "You're enrolled in this course. Yay!")
                    return redirect(reverse_lazy('courses:courses-list'))
                else:
                    messages.add_message(request, messages.WARNING, "You already enrolled.")
                    return redirect(reverse_lazy('courses:courses-list'))
            else:
                messages.add_message((request, messages.WARNING, 'Course does not exist.'))
                return redirect(reverse_lazy('courses:courses-list'))
        except ObjectDoesNotExist:
            messages.add_message((request, messages.ERROR, 'Course not found.'))
            return redirect(reverse_lazy('courses:courses-list'))
