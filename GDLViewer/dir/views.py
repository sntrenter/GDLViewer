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

def list_directories(path):
    directories = []
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            directories.append(file)
    return directories

def display_directory(request, url):
    context = {
        'files':[],
        'dirs':[],
        'prev': ''
    }
    if url[-1] == "/":
        url = url[:-1]
    current_url = url.split("/")[-1]
    context['prev'] = "/dir" + url[:-len(current_url)-1] + "/"
    print("url: " ,url)
    dir_url = url.replace("/gallery-dl","")
    context['dir'] = dir_url 
    #test_img = path + list_files( url[1:])[0]
    print()
    #print("test_img: ", test_img)
    print()
    print("folder url: ","http://127.0.0.1:4444" + dir_url)
    for f in list_files( url[1:]):
        print(f)
        context['files'].append("http://127.0.0.1:4444" + dir_url + "/" + f)
    for d in list_directories( url[1:]):
        print(d)
        context['dirs'].append("/dir" + url + "/" + d)
    #testtxt = f"<img src={test_img} >"
    #return HttpResponse("Hello, world. You're at dir display_directory.: " + url + testtxt)
    return render(request, 'dir.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the dir index.") 