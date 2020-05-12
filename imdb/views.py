from django.shortcuts import render
from django.template import loader
import json
from imdb.models import *
from .utils import get_doughnut_chart_data,get_multi_line_plot_data,get_two_bar_plot_data,get_area_plot_data,get_one_bar_plot_data

def home(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('movie_id')
            movie_obj = Movie.objects.get(movie_id = id)
            movie_obj.delete()
        except Movie.DoesNotExist:
            pass
    movies_objs = list(Movie.objects.all())
    return render(request,'imdb_home.html',{'movies':movies_objs})

def movie(request,movie_id):
    obj = Movie.objects.get(movie_id = movie_id)
    cast_list = list(Cast.objects.filter(movie=obj))
    context = {
        'casts':cast_list,
        'movie_obj':obj
        }
    return render(request,'imdb_movie.html',context)

def actor(request,actor_id):
    obj = Actor.objects.get(actor_id = actor_id)
    cast_list = list(Cast.objects.filter(actor=obj))
    context = {
        'casts':cast_list,
        'actor_obj':obj
    }
    return render(request,'imdb_actor.html',context)

def director(request,name):
    obj = Director.objects.get(name = name)
    movies = Movie.objects.filter(director = obj)
    context = {
        'movies':movies,
        'director_obj': obj
    }
    return render(request,'imdb_director.html',context)

def analytics(request):
    dict_1 = get_doughnut_chart_data()
    dict_3 = get_multi_line_plot_data()
    dict_1.update(dict_3)
    dict_4 = get_two_bar_plot_data()
    dict_1.update(dict_4)
    dict_5 = get_area_plot_data()
    dict_1.update(dict_5)
    dict_6 = get_one_bar_plot_data()
    dict_1.update(dict_6)
    return render(request,'analytics.html',context = dict_1)