from django.urls import path, include
from . import views


urlpatterns = [
    path('trafic_rule_question_detail/<int:question_id>/',
         views.trafic_rule_question_detail, name='trafic_rule_question_detail'),
    path('saved_questions', views.saved_questions, name='saved_questions'),
    path("trafic_rules", views.trafic_rules, name="trafic_rules"),
    path("", views.index, name="home"),
    path('start_quiz', views.start_quiz, name='start_quiz'),
    path('continue_quiz', views.continue_quiz, name='continue_quiz'),
    path('next_question/<int:current_question_id>/',
         views.next_question, name='next_question'),
    path('previous_question/<int:current_question_id>/',
         views.previous_question, name='previous_question'),

]
