from django.contrib import admin

from myapp.models import RoadSign, TraficRule
# Register your models here.

admin.site.register(TraficRule)
admin.site.register(RoadSign)