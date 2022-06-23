from rest_framework.test import APITestCase
from courses.models import Course, Category, Contact, Branch

class TestCourseModels(APITestCase):
    def test_create_course(self):
        course = Course.objects.create(name='course', description='description', logo='logo')
        self.assertIsInstance(course, Course)
        self.assertEqual(course.name, 'course')


class TestCategoryModels(APITestCase):
    def test_create_category(self):
        category = Category.objects.create(name='cooking', imgpath='img')
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, 'cooking')


class TestContactModels(APITestCase):
    def test_create_contact(self):
        contact = Contact.objects.create(suit=1, value='+123')
        self.assertIsInstance(contact, Contact)
        self.assertEqual(contact.value, '+123')

class TestBranchModels(APITestCase):
    def test_create_branch(self):
        branch = Branch.objects.create(latitude=1, longitude=3, address='street 98')
        self.assertIsInstance(branch, Branch)
        self.assertEqual(branch.address, 'street 98')