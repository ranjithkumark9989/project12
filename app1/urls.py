from django.urls import path
from app1.views import *
app_name='aa'

urlpatterns=[
    path('a1_badrinath/',a1_badrinath,name='a1_badrinath'),
    path('a1_bunny/',a1_bunny,name='a1_bunny'),
    path('a1_resugurram/',a1_resugurram,name='a1_resugurram'),
]