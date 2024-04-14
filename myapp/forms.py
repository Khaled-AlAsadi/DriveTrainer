from django import forms
from .models import RoadSign
 
 
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