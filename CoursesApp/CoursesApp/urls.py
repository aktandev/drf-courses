from django.contrib import admin
from django.urls import path
from courses.views import CoursesAPIView, CoursesAPIList
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls'))
]
