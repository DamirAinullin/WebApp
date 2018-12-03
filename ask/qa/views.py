from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request, *args, **kwargs):
    return HttpResponse('index')


def login(request, *args, **kwargs):
    return HttpResponse('login')


def signup(request, *args, **kwargs):
    return HttpResponse('signup')


def question(request, *args, **kwargs):
    return HttpResponse('question id = ' + str(kwargs["id"]))


def ask(request, *args, **kwargs):
    return HttpResponse('ask')


def popular(request, *args, **kwargs):
    return HttpResponse('popular')


def new(request, *args, **kwargs):
    return HttpResponse('new')

