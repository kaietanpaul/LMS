from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    is_instructor = forms.BooleanField(
        label='Instructor', required=False)

    class Meta:
        model = get_user_model()
        fields = ('email', 'fullname', 'is_instructor', 'password')

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            raise ValidationError("Password don't match")

        return password_confirmation

    def save(self, commit=True):
        user = get_user_model().objects.create_user(
            email=self.cleaned_data.get('email'),
            fullname=self.cleaned_data.get('fullname'),
            password=self.cleaned_data.get('password'),
            is_instructor=self.cleaned_data.get('is_instructor')
        )
        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={
            'name': 'username',
            'placeholder': 'Email'
        })
    )

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')

    error_messages = {
        "invalid_login": "Email i hasło nie pasują do żadnego użytkownika."
    }