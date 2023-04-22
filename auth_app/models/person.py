from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.age}"
