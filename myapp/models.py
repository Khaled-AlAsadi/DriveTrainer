from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class TraficRuleQuestion(models.Model):
    question_text = models.CharField(max_length=500,validators=[MinLengthValidator(5), MaxLengthValidator(500)])
    pub_date = models.DateTimeField('date published')
    is_saved = models.BooleanField(default=False)
    link = models.CharField(max_length=500,validators=[MinLengthValidator(5), MaxLengthValidator(500)])
    def __str__(self):
        return self.question_text

class TraficRuleChoice(models.Model):
    question = models.ForeignKey(TraficRuleQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=400,validators=[MinLengthValidator(5), MaxLengthValidator(400)])
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class TraficRuleAnswer(models.Model):
    question = models.ForeignKey(TraficRuleQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_choices = models.ManyToManyField(TraficRuleChoice)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.question.question_text

class TraficRule(models.Model):
    title = models.CharField(max_length=400,validators=[MinLengthValidator(5), MaxLengthValidator(400)])
    sub_title =models.CharField(max_length=400,validators=[MinLengthValidator(5), MaxLengthValidator(400)])
    sub_text = models.TextField(max_length=1000,validators=[MinLengthValidator(5), MaxLengthValidator(1000)],default="Default sub_text")
    image_link = models.CharField(max_length=500,validators=[MinLengthValidator(5), MaxLengthValidator(500)])
    def __str__(self):
        return self.title
    
    
class RoadSign(models.Model):
    title = models.CharField(max_length=400,validators=[MinLengthValidator(5), MaxLengthValidator(400)],blank=False)
    description = models.TextField(max_length=800,validators=[MinLengthValidator(10), MaxLengthValidator(800)],blank=False)
    image_link = models.CharField(max_length=500,validators=[MinLengthValidator(10), MaxLengthValidator(500)],blank=False)
    def __str__(self):
        return self.title