from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('hii bro!!!')


def new(request):
    return HttpResponse('how R you..??')

