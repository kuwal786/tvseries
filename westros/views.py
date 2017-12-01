from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm

def homepage(request):
    return render(request, 'westros/homepage.html')
def westros(request):
    if not request.user.is_authenticated():
        return render(request, 'westros/login.html')
    else:
        anime = Anime.objects.all()
        return render(request, 'westros/westros.html', {'anime': anime})
    return render(request, 'westros/westros.html')
def genres(request):
    return render(request, 'westros/genres.html')
def action(request):
    return render(request, 'westros/action-genre.html')
def comedy(request):
    return render(request, 'westros/comedy-genre.html')
def passwordchange(request):
    return render(request, 'westros/password-change.html')
def tc(request):
    return render(request, 'westros/term-&-conditions.html')
def thanks(request):
    return render(request, 'westros/thanks.html')
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'westros/login.html', context)
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                tvseries = Tvseries.objects.filter(user=request.user)
                return render(request, 'westros/westros.html', {'tvseries': tvseries})
            else:
                return render(request, 'westros/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'westros/login.html', {'error_message': 'Invalid login'})
    return render(request, 'westros/login.html')
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                tvseries = Tvseries.objects.filter(user=request.user)
                return render(request, 'westros/westros.html', {'tvseries': tvseries})
    context = {
        "form": form,
    }
    return render(request, 'westros/register.html', context)
