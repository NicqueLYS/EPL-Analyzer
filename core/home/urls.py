# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from home import views
from .views import MyPasswordChangeView, MyPasswordResetDoneView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    #path('get-seaborn-graph/',views.Api.getSeabornGraph, name='get-seaborn-graph'),
    path('get-seaborn-graph-twon/',views.Api.getSeabornGraphTWon, name='get-seaborn-graph-twon'),
    path('get-seaborn-graph-tdraw/',views.Api.getSeabornGraphTDraw, name='get-seaborn-graph-tdraw'),
    path('get-seaborn-graph-tlost/',views.Api.getSeabornGraphTLost, name='get-seaborn-graph-tlost'),
    path('get-seaborn-graph-tgd/',views.Api.getSeabornGraphTGD, name='get-seaborn-graph-tgd'),
    path('get-seaborn-graph-tpts/',views.Api.getSeabornGraphTPTS, name='get-seaborn-graph-tpts'),
    path('get-seaborn-graph-pposition/',views.Api.getSeabornGraphPPosition, name='get-seaborn-graph-pposition'),
    path('get-seaborn-graph-pcountry/',views.Api.getSeabornGraphPCountry, name='get-seaborn-graph-pcountry'),
    path('change-password/' , MyPasswordChangeView.as_view(), name='password-change-view'),
    path('change-password/done/', MyPasswordResetDoneView.as_view(), name='password-change-done-view'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
