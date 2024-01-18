from django.db import models


class InformationOverdue(models.Model):
    MFO = models.IntegerField()
    Unique = models.IntegerField()
    NameClient = models.CharField(max_length=128)
    Type = models.IntegerField()
    Sum = models.CharField(max_length=128)
    StatusWork = models.CharField(max_length=10)
    StatusTurnover = models.CharField(max_length=10)


class Example(models.Model):
    name = models.CharField(max_length=180)
    sum = models.CharField(max_length=160)
    all = models.IntegerField()



