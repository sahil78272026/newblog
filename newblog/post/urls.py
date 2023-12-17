from django.urls import path
from .views import *

urlpatterns = [
    path('home', home),
    path('create_post/', CreatePost.as_view({'post':'create'})),

]
