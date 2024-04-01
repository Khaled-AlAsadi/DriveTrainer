from django.contrib import admin
from django.contrib import admin
from .models import RoadSignAnswer, RoadSignChoice, RoadSignQuestion, TraficRule, TraficRuleAnswer, TraficRuleChoice, TraficRuleQuestion, TraficRuleText
# Register your models here.

admin.site.register(TraficRuleQuestion)
admin.site.register(TraficRuleChoice)
admin.site.register(TraficRuleAnswer)
admin.site.register(TraficRule)
admin.site.register(TraficRuleText)
admin.site.register(RoadSignQuestion)
admin.site.register(RoadSignChoice)
admin.site.register(RoadSignAnswer)
