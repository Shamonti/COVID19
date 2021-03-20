from django.shortcuts import render
import requests
from django.views.generic import TemplateView 
from .models import economy, economy20, economy21, education, mental_health

# Create your views here.

def index(request):
    data = True
    result = None
    globalSummary = None
    countries = None;
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            globalSummary = json['Global']
            countries = json['Countries']

            data = False
        except:
            data = True
    return render(request , 'covid19App/index.html' ,
                  {'globalSummary' : globalSummary ,
                   'countries' : countries})
    

# def economy(request):
#     return render(request, 'economy.html')

class economyChartView(TemplateView):
    
  template_name = 'covid19App/economy.html'
  
  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['qs'] = economy.objects.all()
        context['economy20_qs'] = economy20.objects.all()
        context['economy21_qs'] = economy21.objects.all()
        return context
    
  # def get_context_data(self, **kwargs):
  #       # Call the base implementation first to get a context
  #       context = super().get_context_data(**kwargs)
  #       # Add in a QuerySet of all the books
  #       context['economy20_qs'] = economy20.objects.all()
  #       return context    
    
class educationChartView(TemplateView):
    
  template_name = 'covid19App/education.html'
  
  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['education_qs'] = education.objects.all()
        return context
    
    
class mental_healthChartView(TemplateView):
    
  template_name = 'covid19App/mental_health.html'
  
  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['mental_health_qs'] = mental_health.objects.all()
        return context