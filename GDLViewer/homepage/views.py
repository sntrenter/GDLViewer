from django.shortcuts import render
from django.http import HttpResponse
import os
import logging

logger = logging.getLogger('django')

def find_root_folders(path):
    root_folders = []
    for root, dirs, files in os.walk(path):
        if not dirs:
            root_folders.append(root)
    return root_folders

def buttontest(request):
    if request.method == 'POST':
        example_input = request.POST.get('example_input', '')
        logger.debug(f"button clicked with input: {example_input}")
        return HttpResponse(f"<p>Button clicked with input: {example_input}</p>")
    else:
        return HttpResponse("<p>Invalid request</p>", status=400)

def index(request):
    #TODO: get the folders to expand from
    test = "test"
    context = {
        'test': test
    }
    return render(request, 'home.html',context)
