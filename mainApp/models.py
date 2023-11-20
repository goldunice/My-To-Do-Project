from django.db import models
from django.contrib.auth.models import User

status = (("Not started", "Not started"), ("In progress", "In progress"), ("Completed", "Completed"))


# Talaba uchun
# kurs, guruh, yonalish
class Talaba(models.Model):
    ism = models.CharField(max_length=255, blank=True)
    kurs = models.PositiveIntegerField(blank=True)
    guruh = models.CharField(max_length=255, blank=True)
    yonalish = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Plan(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=status)
    egasi = models.ForeignKey(Talaba, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
