from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.http.response import JsonResponse 
from .models import User


# Create your views here.

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('userpage')
    else:
        if request.method == 'POST':
            email = request.POST['email']

            password = request.POST['password']
            username = User.objects.get(email=email).username
            

        
            user = auth.authenticate(username=username, password=password)


            if user is not None:
                auth.login(request, user)
                
                return JsonResponse('true', safe=False)
                
            else:
            
                print('no')
                return JsonResponse('false', safe=False)
        return render(request, 'login.html')


def userSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():

               
                return JsonResponse('false1', safe=False)
            elif User.objects.filter(email = email).exists():
               
                return JsonResponse('false2', safe=False)
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, address=address )
                user.save()
               
                
        else:
            messages.info(request, 'pasword not matching')
            print('pasword not matching')
           
            return JsonResponse('false3', safe=False)

        # return redirect('/')
        return JsonResponse('true', safe=False)
    return render(request, 'register.html')

def userPage(request, id=None):
    if request.user.is_authenticated:
        print(request.user)
        if request.method == "DELETE":
            print('dsfdsfasdfsdfasdfsdfa')
        users = User.objects.all()
        return render(request, "user.html", {"users":users})
    else:
        return redirect('login')

def editUser(request, id=None):
    if request.user.is_authenticated:
        username = request.POST['username']
        address = request.POST['address']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.exclude(id = id).filter(username = username).exists():
            return JsonResponse('false1', safe=False)
        elif User.objects.exclude(id = id).filter(email = email).exists():
            return JsonResponse('false2', safe=False)
        else:
            User.objects.filter(id = id).update(username=username,address=address, email=email)
        
        if password1 == password2 and password1 != "":
            user = User.objects.get(id=id)
            user.set_password(password1)
            user.save()
        
        return JsonResponse('true', safe=False)

def deleteUser(request, id):
    if request.user.is_authenticated:
        User.objects.filter(id=id).delete()
        return redirect('userpage')


def logout(request):
    auth.logout(request)
    return redirect("login")
    