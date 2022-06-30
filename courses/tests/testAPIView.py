from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from courses.models import Course


class TestListCreateCourses(APITestCase):


    def setUp(self):
        self.course_url = reverse('courses')


    def test_courses_get(self):
        self.response = self.client.get(self.course_url)
        try:
            self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        except AssertionError:
            return AssertionError(self.response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_course_post(self):
        course_post = {
            "category": [
                {
                    "name": "Programming",
                    "imgpath": "/media"
                }
            ],
            "contact": [
                {
                    "suit": 3,
                    "value": "codem1de@course.com"
                }
            ],
            "branch": [
                {
                    "latitude": 1,
                    "longitude": 2,
                    "address": "chuyi street 12"
                }
            ],
            "name": "CodeMind",
            "description": "Be powerful coder",
            "logo": "logo.png"
        }

        self.response = self.client.post(self.course_url, course_post, format='json')
        try:
            self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        except AssertionError:
            return AssertionError(self.response.status_code, status.HTTP_400_BAD_REQUEST)


class TestCourseDetailView(APITestCase):

    def create_course(self):
        course = Course.objects.create(name='CodeMind',
                                            description='Be powerful coder',
                                            logo='logo.png')
        return course

    def test_course_get(self):
        course = self.create_course()
        self.response = self.client.get(reverse('course', kwargs={'pk':course.id}))
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_course_get_does_not_exist(self):
        self.response = self.client.get(reverse('course', kwargs={'pk': 1}))
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)

    def test_course_delete(self):
        course_data = self.create_course()
        self.response = self.client.delete(reverse('course', kwargs={'pk':course_data.id}))
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_course_delete_does_not_exist(self):
        self.response = self.client.delete(reverse('course', kwargs={'pk': 1}))
        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)