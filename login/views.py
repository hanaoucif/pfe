from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
   
    if request.method == "POST":
      # get the form with its data
      form = LoginForm(request.POST)
      # validate the user inputs 
      if form.is_valid():
         # retrieve the username and password from the form
         username = form.cleaned_data["username"] 
         password = form.cleaned_data["password"]
         # authenticate the user 
         user = authenticate(username=username, password=password)
         # if the authentication is successful, login the user 
         if user is not None:
            
            login(request,user)
            # redirect the user to the home page
            
            request.session["c"]=1
            
            return redirect('acceuil')
          
         
         else:
            error_message = "invalid username or password"
            return render(request,'renm.html',{'form':form,'error_message':error_message})
         
    else:

      form = LoginForm()
      return render(request,"renm.html",{'form':form})
    