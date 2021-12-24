from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

def loginView(request):
    if request.method == 'POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')

        print(f"data received from fe,username={un},password={pw}")
        user=authenticate(username=un,password=pw)
        print(f"user={user}")

        if user is not None:
            login(request,user)
            subject = 'Email verification Done'
            message = f'Hi {user.username}, thanks for visit.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['oshin16196@gmail.com' ]
            send_mail(subject, message, email_from, recipient_list)
            print('mail sent successfully')
            return redirect('show_lap')
        else:
            print('invalid login id or password')
            messages.error(request,'invalid login id or password')
    template_name = 'AuthApp/login.html'
    context = {}
    return render(request, template_name, context)


def registerView(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    template_name='AuthApp/register.html'
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login')