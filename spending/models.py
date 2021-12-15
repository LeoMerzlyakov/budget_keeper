from django.db import models


class Spelling(models.Model):
    payer = models.CharField(max_length=50, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=12, null=True)
    date = models.DateField(null=True)
    description = models.CharField(max_length=1024, null=True)
