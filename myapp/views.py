from urllib.request import HTTPRedirectHandler
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import RoadSignAnswer, RoadSignQuestion, TraficRule, TraficRuleAnswer, TraficRuleChoice, TraficRuleQuestion, TraficRuleText
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    if not isinstance(request.user, AnonymousUser):
        questions = TraficRuleQuestion.objects.all()
        total_traficRules_questions = TraficRuleQuestion.objects.count()
        total_roadSigns_questions = RoadSignQuestion.objects.count()
        answered_questions = TraficRuleAnswer.objects.filter(
            user=request.user, is_answered=True).count()

        answered_roadSignQuestions_questions = RoadSignAnswer.objects.filter(
            user=request.user, is_answered=True).count()
        if answered_roadSignQuestions_questions > 0:
            answered_roadSignQuestions_questions = (
                answered_roadSignQuestions_questions / total_roadSigns_questions) * 100
        else:
            answered_roadSignQuestions_questions = 0

        if total_traficRules_questions > 0:
            progress_percentage = (
                answered_questions / total_traficRules_questions) * 100
        else:
            progress_percentage = 0

        return render(request, 'home.html', {"questions": questions, "progress_percentage": int(progress_percentage), "answered_roadSignQuestions_questions": int(answered_roadSignQuestions_questions)})
    else:
        return HttpResponseRedirect('login')


def trafic_rules(request):
    if not isinstance(request.user, AnonymousUser):
        rules = TraficRule.objects.all()
        rules_texts = TraficRuleText.objects.select_related('sub_title').all()
        print(rules)
        return render(request, 'trafic_rules.html', {"rules": rules, "rule_texts": rules_texts})
    else:
        return HttpResponseRedirect('login')


def saved_questions(request):
    if not isinstance(request.user, AnonymousUser):
        if request.method == "GET":
            saved_questions = TraficRuleQuestion.objects.filter(is_saved=True)
            return render(request, 'saved_questions.html', {'saved_questions': saved_questions})
    else:
        return HttpResponseRedirect('login')


def start_quiz(request):
    first_question = TraficRuleQuestion.objects.first()
    return redirect('trafic_rule_question_detail', question_id=first_question.id)


def continue_quiz(request):
    # Get all answered question IDs
    answered_question_ids = TraficRuleAnswer.objects.values_list(
        'question_id', flat=True)

    # Get the first question that hasn't been answered
    first_unanswered_question = TraficRuleQuestion.objects.exclude(
        id__in=answered_question_ids).first()

    return redirect('trafic_rule_question_detail', question_id=first_unanswered_question.id)


def next_question(request, current_question_id):
    try:
        # id__gt = greater than
        next_question = TraficRuleQuestion.objects.filter(
            id__gt=current_question_id).order_by('id').first()
        if next_question:
            return redirect('trafic_rule_question_detail', question_id=next_question.id)
    except TraficRuleQuestion.DoesNotExist:
        return redirect('question_not_found')


def previous_question(request, current_question_id):
    try:
        # id__lt = less than
        previous_question = TraficRuleQuestion.objects.filter(
            id__lt=current_question_id).order_by('id').first()
        if previous_question:
            return redirect('trafic_rule_question_detail', question_id=previous_question.id)
        else:
            raise Http404("Previous question does not exist")
    except TraficRuleQuestion.DoesNotExist:
        raise Http404("Previous question does not exist")


def trafic_rule_question_detail(request, question_id):
    if not isinstance(request.user, AnonymousUser):
        question = get_object_or_404(TraficRuleQuestion, pk=question_id)
        choices = question.traficrulechoice_set.all()
        last_question_id = TraficRuleQuestion.objects.last().id
        first_question_id = TraficRuleQuestion.objects.first().id
        is_last_question = question_id == last_question_id
        is_first_question = question_id == first_question_id
        message = ''
        is_answered_correctly = False

        if request.method == "POST":
            submitted_answer_id = request.POST.get('choice')
            if submitted_answer_id:
                submitted_choice = TraficRuleChoice.objects.get(
                    pk=submitted_answer_id)
                if submitted_choice.is_correct:
                    message = "Your answer is correct!"
                    is_answered_correctly = True
                    existing_answer = TraficRuleAnswer.objects.filter(
                        question=question, user=request.user).first()
                    if existing_answer:
                        existing_answer.is_answered = True
                        existing_answer.save()
                    else:
                        answer = TraficRuleAnswer.objects.create(
                            question=question, user=request.user, is_answered=True)
                        answer.selected_choices.add(submitted_choice)
                    existing_answer = TraficRuleAnswer.objects.filter(
                        question=question, user=request.user).first()
                    for choice in choices:
                        if choice in existing_answer.selected_choices.all():
                            choice.is_selected = True
                else:
                    message = "Sorry, your answer is wrong."
            else:
                message = "Please select an answer."

        elif request.method == "GET":
            print(is_answered_correctly)
            existing_answer = TraficRuleAnswer.objects.filter(
                question=question, user=request.user).first()
            if existing_answer:
                for choice in choices:
                    if choice in existing_answer.selected_choices.all():
                        choice.is_selected = True
                        is_answered_correctly = True
        return render(request, 'question_detail.html', {'question': question, 'choices': choices, 'message': message, 'is_answered_correctly': is_answered_correctly, 'current_question_id': question_id, "last_question_id": last_question_id, "is_last_question": is_last_question, "is_first_question": is_first_question})
    else:
        return HttpResponseRedirect('login')
