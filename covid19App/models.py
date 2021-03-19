from django.db import models

# Create your models here.
class economy(models.Model):
  name = models.CharField(max_length=220)
  money = models.IntegerField()
  
  def __str__(self):
    return "{}-{}".format(self.name, self.money)
  
  
class education(models.Model):
  name = models.CharField(max_length=220)
  money = models.IntegerField()
  
  def __str__(self):
    return "{}-{}".format(self.name, self.money)
  
  
class mental_health(models.Model):
  name = models.CharField(max_length=220)
  money = models.IntegerField()
  
  def __str__(self):
    return "{}-{}".format(self.name, self.money)