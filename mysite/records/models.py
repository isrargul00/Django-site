from django.db import models
from django.contrib.auth.models import  User
from django.utils import timesince
# Create your models here.


class records_list(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    records = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user} Record {self.records}"

