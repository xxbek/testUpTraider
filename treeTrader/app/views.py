from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    date = datetime.now()
    return HttpResponse(f"Hello, world. You're at the `app` index. Now is {date}")
