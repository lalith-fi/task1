from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import Userform
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_view(request):
    if request.method=='POST':
        if request.POST['cpass'] != request.POST['password']:
            form=Userform()
            
            return render(request,"register.html",{'form':form,'messages':['password does not match']})
        else:
            request.POST._mutable=True
            data=request.POST
            del data['cpass']
            username=data['username']
            
            form=Userform(data,request.FILES)
            if form.is_valid():
                form.save()
                user=User.objects.get(username=username)
                user.set_password(user.password)
                user.save()
            message=["registered"]
            return redirect('login')

            
    else:
        form=Userform()
        
        message=["Fill the Register Form"]
        return render(request,"register.html",{'form':form,'messages':message})


def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        users = authenticate(request, username=username, password=password)
        if users is not None:
            login(request, users)

            return render(request,"profile.html",{'user':users})

        else:
            messages.info(request,'ERROR IN LOGIN!!!')
    return render(request,"login.html")
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
