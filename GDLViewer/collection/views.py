from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import random

def find_root_folders(path):
    root_folders = []
    for root, dirs, files in os.walk(path):
        if not dirs:
            root_folders.append(root)
    return root_folders

def find_root_folders_with_images(path):#garbage code
    root_folders = []
    for root, dirs, files in os.walk(path):
        if not dirs:
            files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
            images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            random_image = random.choice(images) if images else None
            if random_image:
                random_image_path = os.path.join(root, random_image).replace('\\', '/')
                root_folders.append({
                    'name': root,
                    'random_image': "http://localhost:4444/" +  random_image_path.replace("../gallery-dl/", ""),
                })
    return root_folders


# Create your views here.
#need to be running python -m http.server 4444
# to have this running alongside the django server
def index(request):
    path = "../gallery-dl"#project global variable
    root_folders = find_root_folders_with_images(path)
    #print("Root folders in the given path are: ")
    #for folder in root_folders:
    #    print(folder)
    test_image = "http://localhost:4444/coomerparty/onlyfans/aliceoncam/12633615__01_702d02a5-97b8-4d5d-8935-3f957664d29d.jpg"
    print("does test_image exist: ", os.path.exists(test_image))
    print("media root:",settings.MEDIA_ROOT)
    #root_folders = root_folders[:1]
    print("len of root_folders: ", len(root_folders))   
    print("root_folders[0]: ", root_folders[0]) 


    return render(request, 'collection.html',{ 'root_folders': root_folders})
    #return HttpResponse("Hello, world. You're at the collection index.")