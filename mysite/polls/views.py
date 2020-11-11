# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1 align='center'>Hello there This is my first Django Page</h1>")
def second(request):
    return HttpResponse('This is the second page')