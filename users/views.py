from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .forms import UserCreationForm, ProfileForm
from .models import Profile


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Ungültiger Benutzername oder Passwort'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


# def create_user(request):
#     if request.user.is_authenticated:
#         # Benutzer ist bereits eingeloggt, umleiten auf die Startseite
#         return redirect('home')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'create_user.html', {'form': form})

def create_user(request):
    if request.user.is_authenticated:
        # Benutzer ist bereits eingeloggt, umleiten auf die Startseite
        return redirect('home')

    def validate_email_address(value):
        if not value.endswith("@student.uni-halle.de"):
            raise ValidationError(_('Bitte registrieren sie sich mit ihrer Emailadresse der Uni Halle'))

    class RegisterForm(UserCreationForm):
        email = forms.EmailField(validators=[validate_email_address])

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'create_user.html', {'form': form})


def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


def profile_view(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except User.DoesNotExist:
        return render(request, 'user_does_not_exist.html')
    except Profile.DoesNotExist:
        return render(request, 'profile_does_not_exist.html')

    context = {'profile': profile}
    return render(request, 'profile.html', context)
