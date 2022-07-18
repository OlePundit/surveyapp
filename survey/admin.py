from django.contrib import admin
from .models import Survey, Surveyanswers

# Register your models here.
admin.site.register(Survey)
admin.site.register(Surveyanswers)