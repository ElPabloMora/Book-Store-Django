from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout


def signup_view(request):
    
    if request.method == 'POST':
        #here we create the form with a django extension
        form = UserCreationForm(request.POST)
        #valid if the form is valid 
        if form.is_valid():
            # save the user
            user = form.save()
            #With django function login
            login(request, user)
            
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form':form})


def login_view(request):
    
    if request.method == "POST":
        #needed use data=
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
            
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})




def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')

