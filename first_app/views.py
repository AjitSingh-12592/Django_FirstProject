# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

my_dict = {'insert_me': "Hello I am from views.py !",  'insert_me_static': "static static static static"}


def index1(Basic_Flow) :
    return HttpResponse("Basic Flow")


def index2(using_URL_Mapping) :
    return HttpResponse("Using URL Mapping")


def index3(request):
    return render(request, 'index.html', context=my_dict)


def index4(request):
    return render(request, 'first_app/index.html', context=my_dict)


def index5(request):
    return render(request, 'first_app/index_static.html', context=my_dict)


