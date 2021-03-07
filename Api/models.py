from django.db import models
from isodate import parse_duration
from django.contrib.auth.models import User


class customer(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  profile_pic = models.ImageField(default='youlogo.png')
  def __str__(self):
    return self.user.username
class Search(models.Model):
  user = models.ForeignKey(customer,on_delete=models.CASCADE)
  Text_searched= models.CharField(max_length=500,null=True)
  date = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.Text_searched 
  