# views.py
import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse

def display_directory(request, url):
    #base_dir = settings.BASE_DIR / "your_base_directory"  # Set this to your base directory
    #directory_path = base_dir / url

    #if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
    #    raise Http404("Directory does not exist")

    #directory_contents = os.listdir(directory_path)
    #return render(request, 'your_template.html', {'directory_contents': directory_contents, 'directory_path': url})
    print(url)
    return HttpResponse("Hello, world. You're at dir display_directory.: " + url)

def index(request):
    return HttpResponse("Hello, world. You're at the dir index.") 