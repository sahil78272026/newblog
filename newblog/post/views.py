from django.shortcuts import render
from .models import *

# import from DRF
from rest_framework import viewsets
from rest_framework.response import Response

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


class CreatePost(viewsets.ViewSet):

    def create(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        Post.objects.create(title=title, description=description)
        return Response("Post Created!")

class About(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'about.html')
