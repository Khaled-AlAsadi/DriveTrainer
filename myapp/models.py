from django.db import models
from django.contrib.auth.models import User


class TraficRuleQuestion(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    is_saved = models.BooleanField(default=False)
    link = models.CharField(max_length=500,default="")
    def __str__(self):
        return self.question_text

class TraficRuleChoice(models.Model):
    question = models.ForeignKey(TraficRuleQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
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
    title = models.CharField(max_length=400)
    
    def __str__(self):
        return self.title
    
class TraficRuleText(models.Model):
    sub_title = models.ForeignKey(TraficRule,on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    sub_text = models.CharField(max_length=1000,default="Default sub_text")
    image_link = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.sub_title)
    
    
class RoadSign(models.Model):
    title = models.CharField(max_length=400)
    
    def __str__(self):
        return self.title
    
class RoadSignText(models.Model):
    sub_title = models.ForeignKey(RoadSign,on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    sub_text = models.CharField(max_length=1000,default="Default sub_text")
    image_link = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.sub_title)

class RoadSignQuestion(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    link = models.CharField(max_length=500,default="")
    def __str__(self):
        return self.question_text

class RoadSignChoice(models.Model):
    question = models.ForeignKey(RoadSignQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

class RoadSignAnswer(models.Model):
    question = models.ForeignKey(RoadSignQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_choices = models.ManyToManyField(RoadSignChoice)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.question.question_text