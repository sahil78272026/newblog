from django.shortcuts import render
from .models import *

# import from DRF
from rest_framework import viewsets
from rest_framework.response import Response

def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


class CreatePost(viewsets.ViewSet):

    def create(request):
        title = requet.data.get('title')
        description = request.data.get('description')
        Post.objects.create(title=title, description=description)
        return Response("Post Created!")
