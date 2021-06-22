from django.shortcuts import render
from django.http import HttpResponse

from features.models import Info


def index(response):
    return HttpResponse('<h1>Features</h1>')   