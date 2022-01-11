# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('get-seaborn-graph/',views.Api.getSeabornGraph, name='get-seaborn-graph'),
    path('getdata/',views.Api.getData, name='get-data'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
