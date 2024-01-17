from django.db import models


class InformationOverdue(models.Model):
    MFO = models.IntegerField()
    Unique = models.IntegerField()
    NameClient = models.CharField(max_length=128)
    Type = models.CharField(max_length=10)
    Sum = models.FloatField(max_length=128)
    StatusOverdue = models.IntegerField()
    StatusWork = models.CharField(max_length=10)
    StatusTurnover = models.CharField(max_length=10)
