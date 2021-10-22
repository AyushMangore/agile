from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
from nemesis.models import *
from nemesis.form import userform
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def login(request):
    res=render(request,'nemesis/login.html')
    return HttpResponse(res)

def signup(request):
    res=render(request,'nemesis/registration.html')
    return HttpResponse(res)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']

        if(confirm_password == password):
            info = myuser(username=username,email=email,password=password,address=address)
            info.save()

            user = User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('/nemesis')

        else:
            return HttpResponse("Password Mismatch")

    else:
        return render(request,'nemesis/registration.html')

@csrf_exempt
def showDetails(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            request.session['username']=username
            return redirect('/nemesis/info')

        else:
            return redirect('/nemesis')
        
def showInfo(request):
    # if request.method == 'POST':
    if 'username' not in request.session:
        return redirect('/nemesis')
    users = myuser.objects.all()
    data={'users' : users}
    res = render(request,'nemesis/info.html',data)
    return HttpResponse(res)


def update(request,user_id):
    if 'username' not in request.session:
        return redirect('/nemesis')
    user = myuser.objects.get(pk=user_id)
    form=userform(request.POST or None,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/nemesis/info')

    return render(request,'nemesis/edit.html',{'user':user,'form':form})

def delete(request,user_id):
    if 'username' not in request.session:
        return redirect('/nemesis/info')
    user = myuser.objects.get(pk=user_id)
    user.delete()
    return redirect('/nemesis/info')

def logout(request,user_id):
    auth.logout(request)
    return redirect('/nemesis/info')