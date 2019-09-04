from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, StatsUpdateForm
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

# User Routes

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('registerProfile')
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {'form': form})

def registerProfile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            return redirect('registerStats')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "registerProfile.html", {'p_form': p_form})

def registerStats(request):
    if request.method == 'POST':
        s_form = StatsUpdateForm(request.POST, request.FILES, instance=request.user.profile.stats)

        if s_form.is_valid():
            s_form.save()
            logout(request)
            messages.success(request, f'Your account has been created! You can now Log In')
            return redirect('login')

    else:
        s_form = StatsUpdateForm(instance=request.user.profile.stats)

    return render(request, "registerStats.html", {'s_form': s_form})

@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "user_profile.html", context)
