from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import NewUser
# Create your views here.
def register(response):
    if response.method == "POST":
        form = NewUser(response.POST)
        if form.is_valid():
            form.save()
           # return redirect("home/")
    else :
        form=NewUser()
  
    
    return render(response, 'register/register.html', {'form': form})

# Create your views here.
