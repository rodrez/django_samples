from django.db import models


# Create your models here.
class Rate(models.Model):
    data = models.JSONField()
