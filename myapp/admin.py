from django.contrib import admin

from myapp.models import RoadSign, TraficRule,TraficRuleAnswer ,TraficRuleChoice, TraficRuleQuestion
# Register your models here.

@admin.register(RoadSign)
class RoadSignAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image_link']

@admin.register(TraficRule)
class TraficRuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'sub_text','image_link']


@admin.register(TraficRuleQuestion)
class TraficRuleQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'is_saved','link']


@admin.register(TraficRuleChoice)
class TraficRuleChoice(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'is_correct']


@admin.register(TraficRuleAnswer)
class TraficRuleAnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'user', 'is_answered']
