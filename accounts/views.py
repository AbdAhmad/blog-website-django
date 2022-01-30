from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('blogs')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            new_user = form.save()
            new_user = authenticate(username=username,password=password1,)
            login(request, new_user)
            messages.success(request, "Thanks for registering. You are now logged in.")
            return redirect("blogs")
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('blogs')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None:
            if user.check_password(password):
                login(request, user)
                messages.success(request, 'Welcome ' + username)
                return redirect('blogs') 
            else:
                messages.error(request, 'Wrong password')
        else:
            messages.error(request, 'User does not exist')
        return redirect('login')
        
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('login')