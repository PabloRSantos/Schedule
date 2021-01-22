from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} {self.surname}'
