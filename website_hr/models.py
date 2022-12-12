from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

JOB_TYPE = (("1", "Full time"), ("2", "Part time"), ("3", "Internship"))

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=datetime.now)
    filled = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, blank=True)
    tags = models.ManyToManyField(Tag)
    vacancy = models.IntegerField(default=1)

    class Meta:
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse("jobs:jobs-detail", args=[self.id])

    def __str__(self):
        return self.title



class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo_icon = models.CharField(max_length=100)
    logo_color = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name