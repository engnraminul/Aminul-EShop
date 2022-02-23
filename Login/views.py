from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

#Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

#Message Module
from django.contrib import messages

# Model & Form
from Login.models import Profile
from Login.forms import ProfileForm, RegistrationForm


def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account create successfully")
            return HttpResponseRedirect(reverse('Login:signin'))
    return render(request, 'Login/registration.html', context={'form':form})


def signin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Successfully Login')
    return render(request, 'Login/signin.html', context = {'form':form})

@login_required
def signout(request):
    logout(request)
    messages.warning(request, "You are logout successfully!")
    return HttpResponse("Signout User")

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Update successfully")
            form = ProfileForm(instance=profile)
    return render(request, 'Login/update_profile.html', context={'form':form})
