from django.contrib import admin
from .models import economy, economy20, economy21, educationFeb, educationMar, educationApr, mental_healthDepression, mental_healthAnxiety

# Register your models here.

admin.site.register(economy)
admin.site.register(economy20)
admin.site.register(economy21)
admin.site.register(educationFeb)
admin.site.register(educationMar)
admin.site.register(educationApr)
admin.site.register(mental_healthDepression)
admin.site.register(mental_healthAnxiety)