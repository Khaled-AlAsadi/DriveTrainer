from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_choices = models.ManyToManyField(Choice)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.question.question_text

class TraficRule(models.Model):
    title = models.CharField(max_length=400)
    
    def __str__(self):
        return self.title
    
class TraficRuleText(models.Model):
    sub_title = models.ForeignKey(TraficRule,on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    image_link = models.CharField(max_length=2000)
    
    def __str__(self):
        return str(self.sub_title)