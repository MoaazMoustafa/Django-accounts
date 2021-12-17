from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import ProfileForm, Signupform, UserForm
from .models import Profile
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('/accounts/profile')
    else:
        form = Signupform()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})


def profile_edit(request):
    user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        userform = UserForm(request.POST, instance=user)
        profileform = UserForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myform = profileform.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')
    else:
        userform = UserForm(instance=user)
        profileform = ProfileForm(instance=profile)
        return render(request, 'profile_edit.html', {
            'userform': userform,
            'profileform': profileform,
        })
