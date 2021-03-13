from django import forms
from django.db.models import fields
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from profiles.models import Profile

class SingUpForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
        )
    password2 = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
        )
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            user.groups.add(Group.objects.get(name='Customers'))
        return user

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'            
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1'
        ]

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email', 
            'country', 
            'city', 
            'zip_code', 
            'address_first', 
            'address_second', 
            'info',
            ]                       
