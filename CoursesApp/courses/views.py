from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Course
from .serializers import CourseSerializers


class CoursesAPIList(APIView):

    def get_all(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializers(courses, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CoursesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            course = Course.objects.get(id=kwargs['pk'])
        except Course.DoesNotExist:
            return Response({"data": "Course Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializers(course)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            course = Course.objects.get(id=kwargs['pk'])
        except Course.DoesNotExist:
            return Response({"data": "Course Not Found!"}, status=status.HTTP_404_NOT_FOUND)
        course.delete()
        return Response({"data": "Deleted!"})