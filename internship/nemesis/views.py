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
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']

        if(confirm_password == password):
            user = User.objects.create_user(username=username,password=password)
            user.save()

            info = myuser(id=user.id, username=username,phone=phone,email=email,password=password,address=address)
            info.save()

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

        try:
            user_info = myuser.objects.filter(username=username, password=password)
        except:
            user_info = 1
            
        user = auth.authenticate(username=username,password=password)
        print(user)
        
        user_info = user_info.values_list()
        print(user_info)
        if user is not None:
            auth.login(request,user)
            request.session['username']=username
            res=render(request,'nemesis/index.html', {'user_id':user_info[0][0], 'user_name':user_info[0][1]})
            return HttpResponse(res)

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


def logout(request):
    auth.logout(request)
    return redirect('/nemesis/info')



def home(request):
    return render(request,'nemesis/home.html')


def contact(request):
    return render(request,'nemesis/contact.html')


def dashboard(request):
    return render(request,'nemesis/index.html')


def mobiles_info(request, **kwargs):
    dic = {}
    for ele in kwargs:
        print(ele, kwargs[ele])
        dic[ele] = kwargs[ele]
    print(dic)
    details = mobile_details.objects.all()
    data = {'details' : details, 'user_id':dic['user_id']}
    # data['rating'] = int()
    res = render(request,'nemesis/mobiles_category.html',data)
    return res


def review(request,m_id, u_id):
    mob_details=mobile_details.objects.filter(mob_id=m_id)
    data=reviews.objects.filter(mobile_id=m_id, is_verified=True)
    return render(request,'nemesis/reviews.html',{'data':data,'mob':mob_details, 'mobile_id':m_id, 'user_id':u_id})


def give_review(request, m_id, u_id):
    mob_details=mobile_details.objects.filter(mob_id=m_id)
    print(mob_details)
    if request.POST:
        print(request.POST)
        user = myuser.objects.filter(id=u_id).values_list()
        print(user)
        des = request.POST['description']
        heading = request.POST['heading']
        # mobile = mobile_details(mob_id=m_id, name=mob_details[1], rating=mob_details[2], price=mob_details[3], image_link=mob_details[4], product_link=mob_details[5])
        mobile = mobile_details.objects.get(mob_id=m_id)
        review = reviews.objects.create(user_id_id=user[0][0], name=user[0][1], heading=heading, description=des, mobile_id=mobile)
        review.save()
        print('\n')
        print(review)
        return redirect('review', m_id=m_id, u_id=u_id)
    else:
        return render(request, 'nemesis/review.html', {'mobile':mob_details, 'mobile_id':m_id, 'user_id':u_id})

