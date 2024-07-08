# views.py
import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse

def list_files(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
    return files

def display_directory(request, url):
    path = os.path.join(settings.MEDIA_ROOT, url)
    path = "http://127.0.0.1:4444/behance/Malina%20Cosmica%C2%AE/201130925%2080%20GEOMETRIC%20LOGOS/"
    for f in list_files( url[1:]):
        print(f)
    print(path)
    print(url)
    test_img = path + list_files( url[1:])[0]
    print()
    print("test_img: ", test_img)
    print()
    testtxt = f"<img src={test_img} >"
    return HttpResponse("Hello, world. You're at dir display_directory.: " + url + testtxt)

def index(request):
    return HttpResponse("Hello, world. You're at the dir index.") 