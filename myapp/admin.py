from django.contrib import admin
from django.contrib import admin
from .models import Question, Choice, Answer, RoadSignAnswer, RoadSignChoice, RoadSignQuestion, TraficRule, TraficRuleText
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(TraficRule)
admin.site.register(TraficRuleText)
admin.site.register(RoadSignQuestion)
admin.site.register(RoadSignChoice)
admin.site.register(RoadSignAnswer)
