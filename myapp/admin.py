from django.contrib import admin

from myapp.models import RoadSign, createRoadSign
# Register your models here.

@admin.register(RoadSign)
class RoadSignAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image_link']

@admin.register(createRoadSign)
class CreateRoadSignAdmin(admin.ModelAdmin):
    list_display = ['user', 'road_sign']
