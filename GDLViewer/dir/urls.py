# urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<url>.*)', views.display_directory, name='display_directory'),

    #path('<slug:slug>', views.display_directory, name='display_directory'),
    #re_path(r'^dir/(?P<url>.*)/$', views.display_directory, name='display_directory'),
]
