from django.db import models
from django.contrib.auth.models import User

status = (("Not started", "Not started"), ("In progress", "In progress"), ("Completed", "Completed"))


class Plan(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=status)
    egasi= models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
