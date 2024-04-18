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
     path('road_signs',
         views.road_signs_page, name='road_signs'),
     path('road_signs/create',
         views.create_roadSign_view, name='road_signs/create'),
    path('<int:id>/delete/', views.delete_roadSign_view, name='roadsign_delete'),
    path('update/<int:id>/', views.update_roadSign_view, name='update_roadSign_view'),
    path('trafic_rule/create',
         views.create_traficrule_view, name='trafic_rule/create'),
     path('delete/<int:id>/', views.delete_traficrule_view, name='traficrule_delete'),
]
