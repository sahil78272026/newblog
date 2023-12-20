from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# import from DRF
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse



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



@csrf_exempt
def newsLetter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        # email = request.data.get('email')
        print(email)
        NewsLetter.objects.create(email=email)
        posts = Post.objects.all()
        return render(request, 'home.html', {'posts': posts})
