from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy


def register(request, *args, **kwargs):
    if request.method.lower() == 'post':
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            UserModel = get_user_model()
            user = UserModel()
            user.email = email
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'app/register.html', context={'errors': 'Confirm password doesnt match'})
    return render(request, 'app/register.html')


def login_view(request, *args, **kwargs):
    if request.method.lower() == 'post':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'app/login.html', context={'errors': 'Login failed'})
    return render(request, 'app/login.html')


def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required(login_url=reverse_lazy('login'))
def index(request, *args, **kwargs):
    return render(request, 'app/index.html')
