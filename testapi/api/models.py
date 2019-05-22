from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=512, blank=True)
    last_name = models.CharField(max_length=512, blank=True)
    email = models.EmailField(blank=True)
