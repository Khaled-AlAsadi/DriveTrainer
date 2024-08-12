from django import forms
from .models import RoadSign, TraficRule
from django.contrib.auth.forms import AuthenticationForm

# creating a form


class RoadSignForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Title',
        'style': 'width: 300px;',
        'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Subtitle',
        'style': 'width: 300px;',
        'class': 'form-control'}))
    image_link = forms.URLField(widget=forms.URLInput(attrs={
        'placeholder': 'Image Link',
        'style': 'width: 300px;',
        'class': 'form-control'}))

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
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Title',
        'style': 'width: 300px;',
        'class': 'form-control'}))
    sub_title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Subtitle',
        'style': 'width: 300px;',
        'class': 'form-control'}))
    sub_text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Subtext',
        'style': 'width: 300px;',
        'class': 'form-control'}))
    image_link = forms.URLField(widget=forms.URLInput(attrs={
        'placeholder': 'Image Link',
        'style': 'width: 300px;',
        'class': 'form-control'}))

    class Meta:
        model = TraficRule

        fields = [
            "title",
            "sub_title",
            "sub_text",
            "image_link"
        ]


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Ogiltigt användarnamn eller lösenord.",
        'inactive': "Detta konto är inaktiverat.",
    }

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )
