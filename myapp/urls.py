from django.urls import path,include
from . import views


urlpatterns = [
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path("", include("main.urls")),
]