from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('newsletter/', newsLetter),
    path('create_post/', CreatePost.as_view({'post':'create'})),
    path('about/', About.as_view({'get':'list'}), name='about'),
    path('home/', home, name='blogs')


]
