# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from models import *
import os
import uuid
import datetime

def index(request):
    rs = Account.objects.all()
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
    return render_to_response('index.html', locals())

def add_account(request):
    name = request.REQUEST.get("name")
    mao = request.REQUEST.get("mao")
    pi = request.REQUEST.get("pi")
    jing = request.REQUEST.get("jing")
    money = request.REQUEST.get("money")
    time = request.REQUEST.get("time")
    account = Account()
    account.name = name
    account.mao = mao
    account.pi = pi
    account.jing = jing
    account.money = money
    if time:
        account.time = datetime.datetime.strptime(time, "%Y-%m-%d")
    account.save()
    return HttpResponseRedirect("/")

def del_Account(request):
    id = request.REQUEST.get("id")
    Account.objects.filter(id=id).delete()
    return HttpResponseRedirect("/")

def update_Account(request):
    return HttpResponseRedirect("/")







#====================login=============================================
def login(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/admin/")

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect("/admin/")
#======================================================================
