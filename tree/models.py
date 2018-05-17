from django.db import models
from django.utils import timezone

# Create your models here.


class Node(models.Model):
    subject = models.CharField(max_length=255, null=False)
    text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    is_root = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

