import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    id=models.indexes
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    join_date=models.DateTimeField('date joined')
    
    def __str__(self):
        return str(self.id)+" "+self.username+" "+self.role
    def was_joined_recently(self):
        return self.join_date>=timezone.now()-datetime.timedelta(days=1)
    
class Points(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    value=models.IntegerField(default=0)
    deriver=models.CharField(max_length=500)
    
    def __str__(self):
        return self.user.username+" "+str(self.value)+" "+self.deriver