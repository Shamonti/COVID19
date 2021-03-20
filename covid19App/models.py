from django.db import models
# from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

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
    
class educationFeb(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationFeb"
    
class educationMar(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationMar"
    
class educationApr(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationApr"
  
  
class mental_healthDepression(models.Model):
  state = models.CharField(max_length=220)
  value = models.FloatField()
  
  def __str__(self):
    return "{}-{}".format(self.state, self.value)
  
  class Meta:
    verbose_name_plural = "mental_healthDepression"  
    
class mental_healthAnxiety(models.Model):
  state = models.CharField(max_length=220)
  value = models.FloatField()
  
  def __str__(self):
    return "{}-{}".format(self.state, self.value)
  
  class Meta:
    verbose_name_plural = "mental_healthAnxiety"  