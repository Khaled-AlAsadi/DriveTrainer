from django import forms
from .models import RoadSign, TraficRule
 
 
# creating a form
class RoadSignForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = RoadSign
 
        # specify fields to be used
        fields = [
            "title",
            "description",
            "image_link",
        ]

class TraficRuleForm(forms.ModelForm):
    class Meta:
        model = TraficRule
        
        fields = [
            "title",
            "sub_title",
            "sub_text",
            "image_link"
        ]