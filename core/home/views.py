# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView

from django.shortcuts import render
from django.http import HttpResponse
from core.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.views.generic import TemplateView, View 

import numpy as np
import pandas as pd
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sb


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('templates/home/page-500.html')
        return HttpResponse(html_template.render(context, request))


class Api(TemplateView):

    def getSeabornGraphTWon(request):
        file_path = MEDIA_ROOT+"/data/premierleague_tables.csv"
        df = pd.read_csv(file_path)
        graph = sb.catplot(x="Won", y ="Season", hue='Club', data=df, kind='bar')
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        plt.close()
        return response

    def getSeabornGraphTDraw(request):
        file_path = MEDIA_ROOT+"/data/premierleague_tables.csv"
        df = pd.read_csv(file_path)
        graph = sb.catplot(x="Drawn", y ="Season", hue='Club', data=df, kind='bar')
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        plt.close()
        return response

    def getSeabornGraphTLost(request):
        file_path = MEDIA_ROOT+"/data/premierleague_tables.csv"
        df = pd.read_csv(file_path)
        graph = sb.catplot(x="Lost", y ="Season", hue='Club', data=df, kind='bar')
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        plt.close()
        return response
    
    def getSeabornGraphTGD(request):
        file_path = MEDIA_ROOT+"/data/premierleague_tables.csv"
        df = pd.read_csv(file_path)
        graph = sb.catplot(x="Goal Difference", y ="Season", hue='Club', data=df, kind='bar')
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        plt.close()
        return response
    
    def getSeabornGraphTPTS(request):
        file_path = MEDIA_ROOT+"/data/premierleague_tables.csv"
        df = pd.read_csv(file_path)
        graph = sb.catplot(x="Points", y ="Season", hue='Club', data=df, kind='bar')
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        plt.close()
        return response

    def getSeabornGraphPPosition(request):
        file_path = MEDIA_ROOT+"/data/premierleague_player.csv"
        df = pd.read_csv(file_path)
        graph = sb.catplot(x="Season No.", y ="Club", hue='Position', data=df, kind='bar', order=df.Club.value_counts().iloc[:10].index)
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        plt.close()
        return response

    def getSeabornGraphPCountry(request):
        file_path = MEDIA_ROOT+"/data/premierleague_player.csv"
        df = pd.read_csv(file_path)
        graph = sb.catplot(x="Season No.", y ="Club", hue='Nationatility', data=df, kind='bar', order=df.Club.value_counts().iloc[:10].index)
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        plt.close()
        return response

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'home/password-change.html'
    success_url = reverse_lazy('password-change-done-view')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'home/password-reset-done.html'
