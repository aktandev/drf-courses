from rest_framework import serializers
from .models import Course, Category, Contact, Branch


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'imgpath']


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['suit', 'value']


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']



class CourseSerializers(serializers.ModelSerializer):

    category = CategorySerializers()
    contact = ContactSerializers(many=True)
    branch = BranchSerializers(many=True)


    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'category', 'contact', 'branch']

    def create(self, validated_data):
        categories_data = validated_data.pop("category")
        contacts_data = validated_data.pop("contact")
        branches_data = validated_data.pop("branch")
        category =  Category.objects.create(**categories_data)
        course = Course.objects.create(category=category, **validated_data)

        for contact_data in contacts_data:
            Contact.objects.create(course=course, **contact_data)
        for branch_data in branches_data:
            Branch.objects.create(course=course, **branch_data)

        return course