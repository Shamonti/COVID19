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
    
    
class unemploy10(models.Model):
  country10 = models.CharField(max_length=220)
  rate10 = models.FloatField()
  
  def __str__(self):
    return "{}_{}".format(self.country10, self.rate10)
  
  class Meta:
    verbose_name_plural = "unemploy10"
    
    
class unemploy18(models.Model):
  country = models.CharField(max_length=220)
  rate = models.FloatField()
  
  def __str__(self):
    return "{}_{}".format(self.country, self.rate)
  
  class Meta:
    verbose_name_plural = "unemploy18"
    
    
class unemploy19(models.Model):
  country = models.CharField(max_length=220)
  rate = models.FloatField()
  
  def __str__(self):
    return "{}_{}".format(self.country, self.rate)
  
  class Meta:
    verbose_name_plural = "unemploy19"
    
class unemploy20(models.Model):
  country = models.CharField(max_length=220)
  rate = models.FloatField()
  
  def __str__(self):
    return "{}_{}".format(self.country, self.rate)
  
  class Meta:
    verbose_name_plural = "unemploy20"
    
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
    
class educationMay(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationMay"
    
class educationJun(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationJun"
    
class educationJuly(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationJuly"
    
class educationAug(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationAug"
    
class educationSept(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationSept"
    
class educationOct(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationOct"
    
class educationNov(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationNov"
    
    
class educationDec(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationDec"
    
    
class educationJan21(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationJan21"
    
    
class educationFeb21(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationFeb21"
    
    
class educationMar21(models.Model):
  country = models.CharField(max_length=220, blank=True)
  status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
  
  def __str__(self):
    return "{}_{}".format(self.country, self.status)
  
  class Meta:
    verbose_name_plural = "educationMar21"
    
class educationResearch(models.Model):
  situation = models.CharField(max_length=220, blank=True)
  percentage = models.IntegerField()
  
  def __str__(self):
    return "{}_{}".format(self.situation, self.percentage)
  
  class Meta:
    verbose_name_plural = "educationResearch"
  
  
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
    

class mental_healthSuicide18(models.Model):
  state = models.CharField(max_length=220)
  value = models.FloatField()
  
  def __str__(self):
    return "{}-{}".format(self.state, self.value)
  
  class Meta:
    verbose_name_plural = "mental_healthSuicide18"  
    
# 2019        
class mental_healthSuicide(models.Model):
  state = models.CharField(max_length=220)
  value = models.FloatField()
  
  def __str__(self):
    return "{}-{}".format(self.state, self.value)
  
  class Meta:
    verbose_name_plural = "mental_healthSuicide"  
    
class mental_healthSuicide20(models.Model):
  state = models.CharField(max_length=220)
  value = models.FloatField()
  
  def __str__(self):
    return "{}-{}".format(self.state, self.value)
  
  class Meta:
    verbose_name_plural = "mental_healthSuicide20"  