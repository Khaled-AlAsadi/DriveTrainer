from urllib.request import HTTPRedirectHandler
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Question, Choice,Answer, TraficRule, TraficRuleText
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    if not isinstance(request.user, AnonymousUser):
        print(request.user)
        questions = Question.objects.all()
        total_questions = Question.objects.count()
        answered_questions = Answer.objects.filter(user=request.user, is_answered=True).count()
    
        if total_questions > 0:
            progress_percentage = (answered_questions / total_questions) * 100
            print(int(progress_percentage))
        else:
            progress_percentage = 0

        return render(request, 'home.html', {"questions": questions, "progress_percentage": int(progress_percentage)})
    else:
        return HttpResponseRedirect('login')

def trafic_rules(request):
    if not isinstance(request.user, AnonymousUser):
        rules = TraficRule.objects.all()
        rules_texts = TraficRuleText.objects.select_related('sub_title').all()
        print(rules)
        return render(request, 'trafic_rules.html',{"rules":rules, "rule_texts": rules_texts})
    else:
        return HttpResponseRedirect('login')

def saved_questions(request):
    if not isinstance(request.user, AnonymousUser):
        if request.method == "GET":
            saved_questions = Question.objects.filter(is_saved=True)
            return render(request, 'saved_questions.html',{'saved_questions': saved_questions})
    else:
        return HttpResponseRedirect('login') 

def continue_quiz(request):
    questions= Answer.objects.filter(Question,is_answered =False)
    return render(request, 'question_detail.html', {'questions': questions})

def question_detail(request, question_id):
    if not isinstance(request.user, AnonymousUser):
        question = get_object_or_404(Question, pk=question_id)
        choices = question.choice_set.all()
        message = ''
        is_answered_correctly = False

        if request.method == "POST":
                submitted_answer_id = request.POST.get('choice')
                submitted_choice = Choice.objects.get(pk=submitted_answer_id)
                if submitted_choice.is_correct:
                    message = "Your answer is correct!"
                    is_answered_correctly = True
                    existing_answer = Answer.objects.filter(question=question, user=request.user).first()
                    if existing_answer:
                        existing_answer.is_answered = True
                        existing_answer.save()
                    else:
                        answer = Answer.objects.create(question=question, user=request.user, is_answered=True)
                        answer.selected_choices.add(submitted_choice)
                    existing_answer = Answer.objects.filter(question=question, user=request.user).first()
                    for choice in choices:
                        if choice in existing_answer.selected_choices.all():
                            choice.is_selected = True
                else:
                    message = "Sorry, your answer is wrong."

        elif request.method == "GET":
                existing_answer = Answer.objects.filter(question=question, user=request.user).first()
                if existing_answer:
                    for choice in choices:
                        if choice in existing_answer.selected_choices.all():
                            choice.is_selected = True
                    
        return render(request, 'question_detail.html', {'question': question, 'choices': choices, 'message': message, 'is_answered_correctly': is_answered_correctly})
    else:
        return HttpResponseRedirect('login') 