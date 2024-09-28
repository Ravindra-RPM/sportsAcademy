from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from sportapp.models import Coach, Player, Coach
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# index/home page function 
def home(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        n = request.POST['uname'] #kavi
        p = request.POST['upass'] #qwerty123456
        # print(n)
        # print(p)
        u=authenticate(request,username=n, password=p)
        # print(p)
        context = {}
        if u == None:
            context['errmsg'] = 'Invalid Credentials'
            return render(request,'index.html',context)
        else:
            login(request,u)            
            return redirect('/dashboard')


# register page function
def register(request):
    if request.method == 'GET':
        return render (request, 'register.html')
    else:
        n = request.POST['uname']
        t = request.POST['utrain']
        e = request.POST['uemail']
        p = request.POST['upass']
        cp = request.POST['cupass']
        context = {}

        u = User.objects.filter(username=n)
        
        if n == '' or e == '' or p =='' or cp == '' or t =='':
            context['errmsg'] = 'Please fill out all fields'
        elif len(u) != 0:
            context['errmsg'] = 'User already exists, Username must be unique'
        elif len(p) < 8:
            context['errmsg'] = 'Length of password must be at least 8 char long'
        elif p!=cp:
            context['errmsg'] = 'Password and Confirm Password not matching'
        else:
            u=User.objects.create(username=n, email=e)
            u.set_password(p)
            u.save()
            new_u = User.objects.filter(username=n)
            coach_obj = Coach.objects.create(uid=new_u[0],specialization=t)                                    
            context['success'] = 'User created Successfully, Click on login'        
        return render(request,'register.html',context)
 

# logout function 
def user_logout(request):
    logout(request)
    return redirect('/index')

# dashboard function
def dashboard(request):
    context={}
    if request.user.is_authenticated:
        player_obj = Player.objects.all()
        context={}
        context['data']=player_obj
        return render(request,'dashboard.html',context)
    else:
        return redirect('/index')

# player-register function
def create_player(request):
    context={}
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request,'create_player.html')
        else:
            f = request.POST['firstName']
            l = request.POST['lastName']
            a = request.POST['age']
            t = request.POST['team']
            print(t)
            player_obj = Player.objects.create(first_name=f,last_name=l,age=a,team=t)
            player_obj.save()
            return redirect ('/dashboard')
        
    else:
        return redirect('/index')

# edit-player function
def edit_player(request,playerid):
    context={}
    if request.user.is_authenticated:
        if request.method == 'GET':
            player_obj = Player.objects.filter(id=playerid)
            context['data']=player_obj
            return render(request,'edit_player.html',context)
        else:
            f = request.POST['firstName']
            l = request.POST['lastName']
            a = request.POST['age']
            t = request.POST['team']            
            player_obj = Player.objects.filter(id=playerid)
            player_obj.update(first_name=f,last_name=l,age=a,team=t)
            return redirect ('/dashboard')
    else:
        return redirect('/index')

# delete-player function
def delete_player(request,playerid):
    context={}
    if request.user.is_authenticated:
        player_obj = Player.objects.filter(id=playerid)
        player_obj.delete()
        return redirect('/dashboard')
    else:
        return redirect('/index')

# coach-list function
def coach_list(request):
    context={}
    if request.user.is_authenticated:
        if request.method == 'GET':
            coach_obj = Coach.objects.all()
            context['data'] = coach_obj
        return render(request,'coach_list.html',context)
    else:
        return redirect('/index')
    

    
