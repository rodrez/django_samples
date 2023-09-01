from django.contrib import admin

# Register your models here.

from rates.models import Rate

admin.site.register(Rate)
