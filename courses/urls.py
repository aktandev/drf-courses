from django.urls import path
from courses import views

urlpatterns = [
    path('api/v1/courses/', views.CoursesAPIList.as_view(), name='courses'),
    path('api/v1/courses/<int:pk>/', views.CoursesAPIView.as_view(), name='course'),
]