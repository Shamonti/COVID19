from django.db import models

# Create your models here.
class economy(models.Model):
  country = models.CharField(max_length=220)
  gdp = models.FloatField()
  
  def __str__(self):
    return "{}_{}".format(self.country, self.gdp)
  
  class Meta:
    verbose_name_plural = "economy"
    
class economy20(models.Model):
  country20 = models.CharField(max_length=220)
  gdp20 = models.FloatField()
  
  def __str__(self):
    return "{}_{}".format(self.country20, self.gdp20)
  
  class Meta:
    verbose_name_plural = "economy20"
    
class economy21(models.Model):
  country21 = models.CharField(max_length=220)
  gdp21 = models.FloatField()
  
  def __str__(self):
    return "{}_{}".format(self.country21, self.gdp21)
  
  class Meta:
    verbose_name_plural = "economy21"
  
  
class education(models.Model):
  name = models.CharField(max_length=220)
  money = models.IntegerField()
  
  def __str__(self):
    return "{}-{}".format(self.name, self.money)
  
  class Meta:
    verbose_name_plural = "education"
  
  
class mental_health(models.Model):
  name = models.CharField(max_length=220)
  money = models.IntegerField()
  
  def __str__(self):
    return "{}-{}".format(self.name, self.money)
  
  class Meta:
    verbose_name_plural = "mental_health"  