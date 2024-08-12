from django import forms
from .models import RoadSign, TraficRule
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# creating a form

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-postadress")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username': 'Användarnamn',
            'first_name': 'Förnamn',
            'last_name': 'Efternamn',
            'email': 'E-postadress',
            'password1': 'Lösenord',
            'password2': 'Bekräfta lösenord',
        }
        error_messages = {
            'username': {
                'required': 'Användarnamn är obligatoriskt.',
                'unique': 'Detta användarnamn är redan registrerat.',
            },
            'email': {
                'required': 'E-postadress är obligatorisk.',
                'unique': 'Detta e-postadress är redan registrerat.',
            },
            'password1': {
                'required': 'Lösenord är obligatoriskt.',
            },
            'password2': {
                'required': 'Bekräfta lösenord är obligatoriskt.',
                'password_mismatch': 'Lösenorden stämmer inte överens.',
            },
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("E-postadress är redan registrerad.")
        return email

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
