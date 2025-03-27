from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class RequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=255)
    status_code = models.IntegerField()
    response_time = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)  # Optional, to track speed

    def __str__(self):
        return f"{self.user.username} -> {self.endpoint} [{self.status_code}]"
    
class APILog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=255)
    status_code = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.endpoint} [{self.status_code}]"