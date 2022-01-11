# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

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
    def getSeabornGraph(request):
        file_path = MEDIA_ROOT+"/data/premierleague_tables.csv"
        df = pd.read_csv(file_path)
        graph = sb.catplot(x='Season', y ="Won", hue='Club', data=df, kind='bar') # col='Season', col_wrap=5
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        return response

    def getData(request):
        file_path2 = MEDIA_ROOT+"/data/premierleague_player.csv"
        #samp = np.random.randint(100,600,size=(4,5))
        df2 = pd.read_csv(file_path2)
        return HttpResponse(df2.to_html(classes='table table-bordered')) #convert to html table

"""
from django.shortcuts import render
from django.http import HttpResponse
from forward.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.views.generic import TemplateView, View 

import numpy as np
import pandas as pd
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sb

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'combine/index.html', context=None)

##PART 1
class Api(TemplateView):
    # Create your views here.
    def getNums(request):
        n = np.array([2,3,4])
        name1 = "name-1" + str(n[1]) #how to create and parse values 
        return HttpResponse('{"name:":'+name1+',"age":31,"city":"New York"}')

    def getAvg(request):
        s1=request.GET.get("val","")
        if len(s1)==0:
            return HttpResponse("none")
        l1=s1.split(',')
        ar=np.array(l1,dtype=int)

        return HttpResponse(str(np.average(ar)))

    def getGraph(request):
        x = np.arange(0,2 * np.pi, 0.01)
        s = np.cos(x)**2
        plt.plot(x,s)

        plt.xlabel('xlabel(X)')
        plt.ylabel('ylabel(y)')
        plt.title('Basic Graph!')
        plt.grid(True)

        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def getData(request):
        samp = np.random.randint(100,600,size=(4,5))
        df = pd.DataFrame(samp, index=['alex','danny','lina','david'],columns=['Jan','Feb','Mar','Apr','May'])
        return HttpResponse(df.to_html(classes='table table-bordered')) #convert to html table

    def getSeabornGraph(request):
        file_path = MEDIA_ROOT+"/data/titanic_train.csv"
        df = pd.read_csv(file_path)
        graph = sb.factorplot(x='Survived',hue='Sex',data=df, col='Pclass',kind='count')
        response = HttpResponse(content_type="image/jpeg")
        graph.savefig(response, format="png")
        return response

# Part 2: CHART.JS (Involves Javascript)
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'combine/charts.html')

class ChartData(APIView):
    authentication_classes=[]
    permission_classes=[]

    def get(self, request, format=None):
        labels=['January','February',"March","April","May","June","July"]
        chartLabel="My Data"
        chartData=[0,10,5,2,20,30,45]
        data = { # as dictionary
            "labels":labels, 
            "chartLabel":chartLabel, 
            "chartdata":chartData, 
        }
        return Response(data)

# Part 3: Plot.ly (Does not involves Javascript)
from plotly.offline import plot
import plotly.graph_objs as go

class PlotlyChartView(TemplateView):
    def get(self, request, *args, **kwargs):
        x_data=[0,1,2,3]
        y_data=[x**2 for x in x_data]
        plot_div = plot([go.Scatter(
            x=x_data,
            y=y_data,
            mode='lines', # mode='markers+lines' | mode='lines+markers+lines' refer to scatter python documentation
            name='My Plotly Chart',
            opacity=0.8,
            marker_color='green'
        )], output_type='div')

        return render(request, 'combine/plotly.html', context={'plot_div':plot_div})

# Part 4: Plotly Dash (Does not involves Javascript)

# Part 5: Datatables 
import django_tables2 as tables
from book.models import Book
from hello_world.models import User, UserProfileInfo

# Table Class
class BookTable(tables.Table):
    class Meta:
        model = Book
        attrs = {"class": "table-bordered"}

# View
class BookTableView(tables.SingleTableView): # tables = django_tables line 107
    table_class=BookTable
    queryset=Book.objects.all()
    template_name="combine/table.html"

# Table Class
class UserTable(tables.Table): # tables = django_tables line 107
    class Meta:
        model = UserProfileInfo
        attrs = {"class": "table-bordered"}

# View
class UserTableView(tables.SingleTableView): # tables = django_tables line 107
    table_class=UserTable
    # queryset=UserProfileInfo.objects.select_related('user')
    queryset=UserProfileInfo.objects.all()
    template_name="combine/table.html"

"""