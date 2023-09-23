from django.db import models

# Create your models here.


class Person(models.Model):
    """Creating my first model"""
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField("persons' first name",max_length=30)
    last_name = models.CharField(verbose_name="persons' last name", max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER, default=None)


class Dog(models.Model):
    """Creating a dog"""

    COLOR = [
        ('B', 'Black'),
        ('W', 'White'),
        ('R', 'Brown'),
        ('M', 'Mix Color'),
    ]

    name = models.CharField(max_length=30,null=False,unique=True)
    age = models.IntegerField(blank=False)
    color = models.CharField(max_length=1, choices=COLOR, default='M')
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)