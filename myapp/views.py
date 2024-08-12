from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render

from myapp.forms import RoadSignForm, TraficRuleForm
from .models import TraficRule, TraficRuleAnswer
from .models import TraficRuleChoice, TraficRuleQuestion, RoadSign
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm

# Create your views here.
PAGENUMBER = 1


def index(request):
    if not isinstance(request.user, AnonymousUser):
        questions = TraficRuleQuestion.objects.all()
        total_traficRules_questions = TraficRuleQuestion.objects.count()
        answered_questions = TraficRuleAnswer.objects.filter(
            user=request.user, is_answered=True).count()

        if total_traficRules_questions > 0:
            progress_percentage = (
                answered_questions / total_traficRules_questions) * 100
        else:
            progress_percentage = 0

        return render(request, 'home.html',
                      {"questions": questions,
                       "progress_percentage": int(progress_percentage)})
    else:
        return HttpResponseRedirect('login')


def custom_login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Välkommen {username}!')
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)

def trafic_rules(request):
    global PAGENUMBER
    if not isinstance(request.user, AnonymousUser):
        rules = TraficRule.objects.all()
        paginated = Paginator(rules, 5)
        page_number = request.GET.get('page')

        page = paginated.get_page(page_number)
        PAGENUMBER = page_number
        return render(request, 'trafic_rules.html', {'page': page})
    else:
        return HttpResponseRedirect('login')


def start_quiz(request):
    if not isinstance(request.user, AnonymousUser):

        first_question = TraficRuleQuestion.objects.first()
        return redirect('trafic_rule_question_detail',
                        question_id=first_question.id)
    else:
        return redirect('login')


def continue_quiz(request):
    if not isinstance(request.user, AnonymousUser):

        # Get all answered question IDs
        # Flat retrives a single field
        answered_question_ids = TraficRuleAnswer.objects.values_list(
            'question_id', flat=True)

        # Get the first question that hasn't been answered
        first_unanswered_question = TraficRuleQuestion.objects.exclude(
            id__in=answered_question_ids).first()

        return redirect('trafic_rule_question_detail',
                        question_id=first_unanswered_question.id)
    else:
        return redirect('login')


def next_question(request, current_question_id):
    if not isinstance(request.user, AnonymousUser):

        try:
            # id__gt = greater than
            next_question = TraficRuleQuestion.objects.filter(
                id__gt=current_question_id).order_by('id').first()
            if next_question:
                return redirect('trafic_rule_question_detail',
                                question_id=next_question.id)
        except TraficRuleQuestion.DoesNotExist:
            return redirect('question_not_found')
    else:
        return redirect('login')


def previous_question(request, current_question_id):
    if not isinstance(request.user, AnonymousUser):

        try:
            # id__lt = less than
            previous_question = TraficRuleQuestion.objects.filter(
                id__lt=current_question_id).order_by('-id').first()
            if previous_question:
                return redirect('trafic_rule_question_detail',
                                question_id=previous_question.id)
            else:
                raise Http404("Previous question does not exist")
        except TraficRuleQuestion.DoesNotExist:
            raise Http404("Previous question does not exist")
    else:
        return redirect('login')


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
                            question=question, user=request.user,
                            is_answered=True)
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
            existing_answer = TraficRuleAnswer.objects.filter(
                question=question, user=request.user).first()
            if existing_answer:
                for choice in choices:
                    if choice in existing_answer.selected_choices.all():
                        choice.is_selected = True
                        is_answered_correctly = True
        return render(request,
                      'question_detail.html',
                      {'question': question,
                       'choices': choices,
                          'message': message,
                          'is_answered_correctly': is_answered_correctly,
                          'current_question_id': question_id,
                          "last_question_id": last_question_id,
                          "is_last_question": is_last_question,
                          "is_first_question": is_first_question})
    else:
        return HttpResponseRedirect('login')


def road_signs_page(request):
    global PAGENUMBER
    if not isinstance(request.user, AnonymousUser):
        road_signs = RoadSign.objects.all()
        paginated = Paginator(road_signs, 5)
        page_number = request.GET.get('page')
        PAGENUMBER = page_number
        page = paginated.get_page(page_number)
        return render(request, 'road_signs_page.html', {'page': page})
    else:
        return HttpResponseRedirect('login')

# create view for RoadSign


def create_roadSign_view(request):
    if not isinstance(request.user, AnonymousUser) and request.user.is_staff:

        # dictionary for initial data with
        # field names as keys
        context = {}

        # add the dictionary during initialization
        form = RoadSignForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'väggmärket skapades!')
            return redirect('road_signs')
        storage = messages.get_messages(request)
        storage.used = True
        context['form'] = form
        context["PAGENUMBER"] = PAGENUMBER

        return render(request, "create_roadsign_view.html", context)
    else:
        return HttpResponseRedirect('login')


# delete view for RoadSign
def delete_roadSign_view(request, id):
    if not isinstance(request.user, AnonymousUser) and request.user.is_staff:

        # dictionary for initial data with
        # field names as keys
        context = {}

        # fetch the object related to passed id
        obj = get_object_or_404(RoadSign, id=id)

        if request.method == "POST":
            # delete object
            obj.delete()
            # after deleting redirect to
            # home page
            messages.success(request, 'väggmärket raderades!')
            return redirect('road_signs')
        storage = messages.get_messages(request)
        storage.used = True
        context["PAGENUMBER"] = PAGENUMBER
        return render(request, "delete_roadsign_view.html", context)
    else:
        return redirect('login')

# update view for RoadSign


def update_roadSign_view(request, id):
    if not isinstance(request.user, AnonymousUser) and request.user.is_staff:

        context = {}

        # Fetch the object related to the passed id
        obj = get_object_or_404(RoadSign, id=id)

        # Pass the object as an instance in the form
        form = RoadSignForm(request.POST or None, instance=obj)
        # Save the data from the form and redirect to detail_view
        if form.is_valid():
            form.save()
            messages.success(request, 'väggmärket uppdaterades!')
            return redirect('road_signs')
        storage = messages.get_messages(request)
        storage.used = True
        # Add form dictionary to context
        context["form"] = form
        context["PAGENUMBER"] = PAGENUMBER

        return render(request, "update_roadsign_view.html", context)
    else:
        return redirect('login')


# create view for TraficRule
def create_traficrule_view(request):
    if not isinstance(request.user, AnonymousUser) and request.user.is_staff:

        # dictionary for initial data with
        # field names as keys
        context = {}

        # add the dictionary during initialization
        form = TraficRuleForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'trafikregler skapades!')
            return redirect('trafic_rules')
        storage = messages.get_messages(request)
        storage.used = True
        context['form'] = form
        context["PAGENUMBER"] = PAGENUMBER
        return render(request, "create_traficrule_view.html", context)
    else:
        return redirect('login')


# delete view for TraficRule
def delete_traficrule_view(request, id):
    if not isinstance(request.user, AnonymousUser) and request.user.is_staff:

        context = {}

        # Fetch the TraficRule object related to the passed id
        obj = get_object_or_404(TraficRule, id=id)

        if request.method == "POST":
            # Delete the object
            obj.delete()
            # After deleting, redirect to the home page
            messages.success(request, 'trafikregler raderades!')
            return redirect('trafic_rules')
        storage = messages.get_messages(request)
        storage.used = True
        context["PAGENUMBER"] = PAGENUMBER
        return render(request, "delete_traficrule_view.html", context)
    else:
        return redirect('login')


# update view for RoadSign
def update_traficRule_view(request, id):
    if not isinstance(request.user, AnonymousUser) and request.user.is_staff:

        context = {}

        # Fetch the object related to the passed id
        obj = get_object_or_404(TraficRule, id=id)

        # Pass the object as an instance in the form
        form = TraficRuleForm(request.POST or None, instance=obj)
        # Save the data from the form and redirect to detail_view
        if form.is_valid():
            form.save()
            messages.success(request, 'trafikregler uppdaterades!')
            return redirect('trafic_rules')
        storage = messages.get_messages(request)
        storage.used = True
        # Add form dictionary to context
        context["form"] = form
        context["PAGENUMBER"] = PAGENUMBER
        return render(request, "update_traficrule_view.html", context)
    else:
        return redirect('login')
