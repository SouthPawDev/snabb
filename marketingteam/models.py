from django.db import models
from django.urls import reverse
from franchises.models import Franchise
# Create your models here.


class Smr(models.Model):
    smr_pic = models.ImageField(upload_to='smr_pics', blank=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=12)
    smr_franchise = models.ForeignKey(Franchise, related_name='smrs', on_delete='PROTECT')
    smr_car = models.CharField(max_length=256)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("marketingteam:detail", kwargs={'pk': self.pk})
