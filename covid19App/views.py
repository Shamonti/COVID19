from django.shortcuts import render
import requests
from django.views.generic import TemplateView 
from .models import economy, economy20, economy21, unemploy10, unemploy18, unemploy19, unemploy20, educationFeb, educationMar, educationApr, educationMay, educationJun, educationJuly, educationAug, educationSept, educationOct, educationNov, educationDec, educationJan21, educationFeb21, educationMar21, educationResearch, mental_healthDepression, mental_healthAnxiety, mental_healthSuicide18, mental_healthSuicide, mental_healthSuicide20

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
        context['unemploy10_qs'] = unemploy10.objects.all()
        context['unemploy18_qs'] = unemploy18.objects.all()
        context['unemploy19_qs'] = unemploy19.objects.all()
        context['unemploy20_qs'] = unemploy20.objects.all()
        return context

    
class educationChartView(TemplateView):
    
  template_name = 'covid19App/education.html'
  
  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['educationFeb_qs'] = educationFeb.objects.all()
        context['educationMar_qs'] = educationMar.objects.all()
        context['educationApr_qs'] = educationApr.objects.all()
        context['educationMay_qs'] = educationMay.objects.all()
        context['educationJun_qs'] = educationJun.objects.all()
        context['educationJuly_qs'] = educationJuly.objects.all()
        context['educationAug_qs'] = educationAug.objects.all()
        context['educationSept_qs'] = educationSept.objects.all()
        context['educationOct_qs'] = educationOct.objects.all()
        context['educationNov_qs'] = educationNov.objects.all()
        context['educationDec_qs'] = educationDec.objects.all()
        context['educationJan21_qs'] = educationJan21.objects.all()
        context['educationFeb21_qs'] = educationFeb21.objects.all()
        context['educationMar21_qs'] = educationMar21.objects.all()
        context['educationResearch_qs'] = educationResearch.objects.all()
        
        return context
    
    
class mental_healthChartView(TemplateView):
    
  template_name = 'covid19App/mental_health.html'
  
  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['mental_healthDepression_qs'] = mental_healthDepression.objects.all()
        context['mental_healthAnxiety_qs'] = mental_healthAnxiety.objects.all()
        context['mental_healthSuicide18_qs'] = mental_healthSuicide18.objects.all()
        context['mental_healthSuicide_qs'] = mental_healthSuicide.objects.all()
        context['mental_healthSuicide20_qs'] = mental_healthSuicide20.objects.all()
        return context