from django.urls import path
from app2.views import *
app_name='allu'

urlpatterns=[
    path('a2_dj/',a2_dj,name='a2_dj'),
    path('a2_pushpa/',a2_pushpa,name='a2_pushpa'),
    path('a2_meghana/',a2_meghana,name='a2_meghana'),
]