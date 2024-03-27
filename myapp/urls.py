from django.urls import path,include
from . import views


urlpatterns = [
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('saved_questions',views.saved_questions, name='saved_questions'),
    path("trafic_rules", views.trafic_rules , name="trafic_rules"),
    path("", views.index , name="home"),
]