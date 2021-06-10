from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=500)
    link = models.URLField()
    image = models.URLField()
    description = models.TextField()
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=500)
    tag = models.CharField(
        max_length=4,
        choices=[
        ('des', 'Men'), ('dev', 'Women'), ('gra', 'Tech & stuff')
    ])

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    description = models.TextField()
    linked_in_url = models.URLField()
    image = models.ImageField()
    github_url = models.URLField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    icon = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=500)
    logo = models.ImageField()

    def __str__(self):
        return self.name