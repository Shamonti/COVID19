from django.contrib import admin
from .models import economy, education, mental_health

# Register your models here.

admin.site.register(economy)
admin.site.register(education)
admin.site.register(mental_health)