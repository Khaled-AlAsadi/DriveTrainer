from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Question , Choice

# Create your views here.


def index(request):
    questions = Question.objects.all()
    print(questions)
    return render(request, 'home.html',{"questions":questions})


def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    # Retrieve all choices related to the question
    choices = question.choice_set.all()
    return render(request, 'question_detail.html', {'question': question, 'choices': choices})

