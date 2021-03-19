from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from covid19App.views import economyChartView, educationChartView, mental_healthChartView
from covid19App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index, name='index'),
    path('economy/', economyChartView.as_view(), name='economy'),
    path('education/', educationChartView.as_view(), name='education'),
    path('mental_health/', mental_healthChartView.as_view(), name='mental_health'),
    
    # path('' , include('covid19App.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
