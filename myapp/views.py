from urllib.request import HTTPRedirectHandler
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Question, Choice,Answer
from django.contrib.auth.models import AnonymousUser

# Create your views here.


def index(request):
    if not isinstance(request.user, AnonymousUser):
        print(request.user)
        questions = Question.objects.all()
        print(questions)
        return render(request, 'home.html', {"questions": questions})
    else:
        return HttpResponseRedirect('login')

def saved_questions(request):
    if not isinstance(request.user, AnonymousUser):
        if request.method == "GET":
            saved_questions = Question.objects.filter(is_saved=True)
            return render(request, 'saved_questions.html',{'saved_questions': saved_questions})
    else:
        return HttpResponseRedirect('login') 

def question_detail(request, question_id):
    if not isinstance(request.user, AnonymousUser):
        question = Question.objects.get(pk=question_id)
        # Retrieve all choices related to the question
        choices = question.choice_set.all()
        message = None

        if request.method == "POST":
            submitted_answer_id = request.POST.get('choice')
            print(submitted_answer_id)
            submitted_choice = Choice.objects.get(pk=submitted_answer_id)
            if submitted_choice.is_correct:
                print("CORRECT")
                message = "Your answer is correct!"
                existing_answer = Answer.objects.filter(question=question, user=request.user).first()
                if existing_answer and not existing_answer.is_answered:
                    existing_answer.is_answered = True
                    existing_answer.save()
                elif not existing_answer:
                    answer = Answer.objects.create(question=question, user=request.user, is_answered=True)
                    answer.selected_choices.add(submitted_choice)
            else:
                message = "Sorry, your answer is wrong."
                print("WRONG")
                
        if request.method == "GET":
            question = Question.objects.get(pk=question_id)
            choices = question.choice_set.all()
        return render(request, 'question_detail.html', {'question': question, 'choices': choices, 'message': message})
    else:
        return HttpResponseRedirect('login') 