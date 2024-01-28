from django.shortcuts import render,redirect
from django.template import loader
from .forms import formfile
from .models import archives

# Create your views here
def search(request):
    return render(request,'search.html',{})
def export(request):
    export =archives.objects.all()
    return render(request,'export.html',{'inform':export})

def home(request):
    if request.method =="POST":
        form =formfile(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form =formfile()
           
        
            
    else:
        form=formfile()

    return render(request, 'home.html', {'form': form})

