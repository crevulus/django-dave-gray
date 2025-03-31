from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:list')
        else:
            print(form.errors)
    else:
      form = UserCreationForm()

    return render(request, 'users/register.html', {"form": form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print (form.get_user())
            login(request, form.get_user())
            if "nextzy" in request.POST:
                return redirect(request.POST.get("nextzy"))
            else:
                return redirect('posts:list')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {"form": form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse_lazy('home'))

