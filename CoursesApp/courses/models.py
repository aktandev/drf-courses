from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=250)
    imgpath = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True, related_name='branch')

    def __str__(self):
        return self.address


class Contact(models.Model):

    class Suit(models.IntegerChoices):
        PHONE= 1,
        FACEBOOK = 2,
        EMAIL = 3

    suit = models.IntegerField(choices=Suit.choices)
    value = models.CharField(max_length=250)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True, related_name='contact')

    def __str__(self):
        return self.value


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    logo = models.CharField(max_length=250 ,blank=True)

    def __str__(self):
        return self.name
