from django.db import models
from basic.models import Member


class Schedule(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    available = models.DateTimeField()