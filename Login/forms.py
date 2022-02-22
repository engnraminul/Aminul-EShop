from django.forms import ModelForm
from Login.models import User, Profile


from django.contrib.auth.forms import UserCreationForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ('email', 'password_1', 'password_2',)
