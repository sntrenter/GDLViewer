from django.shortcuts import render
from django.http import HttpResponse
import os
import logging
from .models import URL
import re

logger = logging.getLogger('django')

def find_root_folders(path):
    root_folders = []
    for root, dirs, files in os.walk(path):
        if not dirs:
            root_folders.append(root)
    return root_folders

def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def buttontest(request):
    if request.method == 'POST':
        example_input = request.POST.get('example_input', '')
        logger.debug(f"button clicked with input: {example_input}")
        #add the input to the database
        if is_valid_url(example_input):
            U = URL(url=example_input)
            U.save()
            return HttpResponse(f"<p>URL Saved: {example_input}</p>", status=200)
        else:
            return HttpResponse(f"<p>Button clicked with input: {example_input}</p> <br> <p> URL not valid </p>")
    else:
        return HttpResponse("<p>Invalid request</p>", status=400)

def index(request):
    #TODO: get the folders to expand from
    test = "test"
    context = {
        'test': test
    }
    #get the items from the homepage_url table
    urls = URL.objects.all()
    context['urls'] = urls
    #logger.debug(f"URLs: {urls}")
    #print("test")
    return render(request, 'home.html',context)
