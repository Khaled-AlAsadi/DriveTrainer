from django.contrib import admin

from myapp.models import RoadSign
# Register your models here.

@admin.register(RoadSign)
class RoadSignAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image_link']

