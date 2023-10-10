from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse (" tell me how good it feels to be needed ")