from enum import unique

from django.db import models
from django.utils import timezone


# Create your models here.


class Work(models.Model):
    name = models.CharField(unique=True, max_length=128)
    summary = models.CharField(max_length=255, null=True)
    is_individual = models.BooleanField(default=True)
    limit_date = models.DateField(default=timezone.now)
    # members = models.ManyToManyField()
    #
    # class Meta:
    #     unique_together = ('name', )


class Node(models.Model):
    subject = models.CharField(max_length=255, null=False)
    text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    is_root = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
