from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from courses import views

urlpatterns = [
    path('api/v1/courses/', views.CoursesAPIList.as_view()),
    path('api/v1/courses/<int:pk>/', views.CoursesAPIView.as_view()),
]