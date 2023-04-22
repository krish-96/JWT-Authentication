from django.db import models

# Create your models here.

TV_COMPANIES = [('samsung', 'SAMSUNG'), ('tcl', 'TCL'), ('redmi', 'REDMI'), ('lg', 'LG'), ('sony', 'SONY')]


class TeleVision(models.Model):
    company = models.CharField(choices=TV_COMPANIES, default='lg', max_length=256)
    model = models.CharField(max_length=256, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Company : {self.company} | model : {self.model} | Price : {self.price}"
