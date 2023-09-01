from django.db import models

from rates.schema import RATE_SCHEMA
from rates.validator import JSONSchemaValidator


# Create your models here.
class Rate(models.Model):
    data = models.JSONField(validators=[JSONSchemaValidator(limit_value=RATE_SCHEMA)])
    credit_union = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.credit_union} - Enhanced Rate"
