from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class psa_members(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    employer = models.CharField(max_length=200)
    membership_number = models.CharField(max_length=5)
    application_date = models.DateTimeField(blank=True, null=True)


def __str__(self):
    return self.name
