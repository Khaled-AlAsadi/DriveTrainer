from django.contrib import admin

from myapp.models import RoadSign, TraficRule
# Register your models here.

@admin.register(RoadSign)
class RoadSignAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image_link']

@admin.register(TraficRule)
class TraficRuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'sub_text','image_link']
