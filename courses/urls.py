from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses-list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course-delete'),
    path('create/', views.CourseCreateView.as_view(), name='course-create'),
    path('edit/<int:pk>/', views.CourseUpdateView.as_view(), name='course-update'),
    path('<slug:course_slug>/join/', views.student_enrollment, name='student-enrollment'),
]
