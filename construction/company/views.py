from django.shortcuts import render,redirect
from .forms import Applicantsform
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    form=UserCreationForm()
    return render(request,"company/signup.html")

def homepage(request):
   
    submitted = False
    if request.method == "POST":
         form = Applicantsform(request.POST)
         if form.is_valid():
            form.save()
            return redirect('/?submitted=True')
    else:        
         form= Applicantsform
         if 'submitted' in request.GET:
            submitted=True
    return render(request,"company/index.html", {'form':form, 'submitted':submitted})

def about(request):
    return render(request, "company/about.html")

def blog(request):
    return render(request, "company/blog.html")

def contact(request):
    return render(request, "company/contact.html")

def projects(request):
    return render(request, "company/projects.html")

def services(request):
    return render(request, "company/services.html")
