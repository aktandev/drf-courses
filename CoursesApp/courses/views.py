from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .models import Course
from .serializers import CourseSerializers


class CoursesAPIList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CoursesAPIView(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except CourseSerializers:
            return Response('Object not found',status=status.HTTP_404_NOT_FOUND)


    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializers(course)
        return Response(serializer.data)



    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(f'object with id: {pk} has been deleted' ,status=status.HTTP_204_NO_CONTENT)



    # def delete(self, request, pk, format=None, *args, **kwargs):
    #     try:
    #         course = self.get_object(pk=pk)
    #         course.delete()
    #         return Response( 'Object has been deleted ', status=status.HTTP_204_NO_CONTENT)
    #     except CourseSerializers:
    #         return Response('Object not found', status=status.HTTP_404_NOT_FOUND)


class DelCourseAPIView(APIView):
    pass


