from django.contrib import admin

from .models import Node
# Register your models here.

#
# class NodeAdmin(admin.ModelAdmin):
#     fields = ['subject']


admin.site.register(Node)
