from django.db import models
from django.contrib.auth.models import User, AbstractUser

status = (("Not started", "Not started"), ("In progress", "In progress"), ("Completed", "Completed"))


# Talaba uchun
# kurs, guruh, yonalish
class Talaba(AbstractUser):
    ism = models.CharField(max_length=255)
    kurs = models.PositiveIntegerField()
    guruh = models.CharField(max_length=255)
    yonalish = models.CharField(max_length=255)
    first_name = None
    last_name = None
    last_login = None

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
