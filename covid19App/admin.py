from django.contrib import admin
from .models import economy, economy20, economy21, education, mental_health

# Register your models here.

admin.site.register(economy)
admin.site.register(economy20)
admin.site.register(economy21)
admin.site.register(education)
admin.site.register(mental_health)