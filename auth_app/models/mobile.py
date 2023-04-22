from django.db import models
from .company import Company

class Mobile(models.Model):
    brand = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    ram = models.IntegerField(null=False, blank=False)
    rom = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Mobile Brand : {self.brand} | RAM:{self.ram} | ROM:{self.rom}"
