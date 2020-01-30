from django.db import models
from django.urls import reverse
# Create your models here.


# About Model
class AboutMe(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

        def __str__(self):
            return "About Me"


# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About Service")

    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work Title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


# Client Model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client Name")
    description = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name
