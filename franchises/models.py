from django.db import models
from django.urls import reverse
# Create your models here.


class Franchise(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("franchises:detail", kwargs={'pk': self.pk})
