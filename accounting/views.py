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
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
    rs = Account.objects.order_by("-id")

    filter_name = request.REQUEST.get("filter_name", "")
    filter_time = request.REQUEST.get("filter_time", "")

    if filter_name:
        rs = rs.filter(name=filter_name)

    if filter_time:
        time1, time2 = filter_time.split()
        time1 = datetime.datetime.strptime(time1, "%Y-%m-%d")
        time2 = datetime.datetime.strptime(time2, "%Y-%m-%d")
        rs = rs.filter(time__gte=time1)
        rs = rs.filter(time__lte=time2)

    total_mao = 0
    total_pi = 0
    total_jing = 0
    total_money = 0
    for r in rs:
        try:
            total_mao += float(r.mao)
        except:
            pass
        try:
            total_pi += float(r.pi)
        except:
            pass
        try:
            total_jing += float(r.jing)
        except:
            pass
        try:
            total_money += float(r.money)
        except:
            pass

    namelist = []
    for account in Account.objects.all():
        if account.name not in namelist:
            namelist.append(account.name)

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
    else:
        account.time = datetime.datetime.now()
    account.save()
    return HttpResponseRedirect("/")

def del_account(request):
    id = request.REQUEST.get("id")
    Account.objects.filter(id=id).delete()
    return HttpResponseRedirect("/")

def update_account(request):
    return HttpResponseRedirect("/")


def pay(request):
    id = request.REQUEST.get("id")
    account = Account.objects.get(id=id)
    account.status = "已支付"
    account.save()
    return HttpResponseRedirect("/")

def unpaid(request):
    id = request.REQUEST.get("id")
    account = Account.objects.get(id=id)
    account.status = "未支付"
    account.save()
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
