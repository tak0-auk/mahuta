from django.contrib import admin

# Register your models here.
from .models import Work, Node

admin.site.register(Work)
admin.site.register(Node)
