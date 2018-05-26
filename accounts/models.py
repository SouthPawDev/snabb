from django.db import models
from django.contrib.auth import models as acc_models

# Create your models here.


class User(acc_models.User, acc_models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
