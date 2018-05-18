from django.db import models

# Create your models here.


class Work(models.Model):
    name = models.CharField(max_length=128)
    is_individual = models.BooleanField()
    #
    # class Meta:
    #     unique_together = ('name', )
