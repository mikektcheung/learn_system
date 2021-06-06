from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import *
from django.db.models import Sum


# Create your views here.

def index(request):
    return render(request, 'main/welcome.html')

accessdeniedurl = '/'

def login(request):
    check = False
    try:
        user = request.GET['u']
        p = User.objects.filter(username = user)
        if len(p) == 1:
            p = p[0]
            p = user_profile.objects.get(user = p)
            check = True
    except:
        user = ''
    if check:
        error_message = ''
        if request.user.groups.filter(name='cheung_family').exists():
            return redirect('main') 
        elif request.method == 'POST':
            pw = request.POST.get('password',None)
            if len(pw) == 3:
                pw = '0'+ pw
            user_login = authenticate(username=user, password=pw)
            if user_login is not None:
                auth_login(request, user_login)
                return redirect('main')
            else:
                error_message = 'Password is wrong'
        return render(request, 'main/login.html', locals())
    else:
        return redirect('index')

def logout(request):
    auth_logout(request)  
    return redirect('index')

@login_required(login_url='/')
def main(request):
    if request.user.groups.filter(name='cheung_family').exists():
        p = user_profile.objects.get(user = request.user)
        try:
            point = redeem.objects.filter(user = request.user).aggregate(score=Sum('score'))
            point = int(point['score'])
        except:
            point = 0
        try:
            eng_quiz = eng_quiz_result.objects.filter(user = request.user)
        except:
            eng_quiz = []
        try:
            #children = redeem.objects.values('user').annotates(score=Sum('score'))
            children = user_profile.objects.values('pk', 'user__first_name').annotate(score= Sum('redeem__score')).filter(parent = p)
            #children = user_profile.objects.values_list('pk', 'user__first_name').annotate(Sum('redeem__score'))
        except:
            children = []

        #print(children)
        return render(request, 'main/main.html', locals())
    else:
        return redirect('index')

def redeem_change(request, pk):
    if request.user.groups.filter(name='cheung_family').exists():
        p = user_profile.objects.get(user = pk)
        t = request.GET['type']
        #print(t)
        #print(p)
        rtype = redeem_type.objects.filter(type=t).order_by('name', 'score')
        #print(rtype)
        if request.method == 'POST':
            change = request.POST.get('score', None)
            content = request.POST.get('content', None)
            score = redeem_type.objects.get(id = int(change))
            redeem.objects.create(user=p, type=score, score=score.score, content=content)
            #print(change)
            return redirect('main')
        return render(request, 'main/redeem_change.html', locals())
    else:
        return redirect('index')
