from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import MoviesForm
from . models import Movies


def index(request):
    movies = Movies.objects.all()
    context = {
        'project_name': "Movies App",
        'title': "Home",
        'movies_list': movies,
    }
    return render(request, "baseapp/index.html", context)


def details(request, pk):
    data = Movies.objects.get(pk=pk)
    context = {
        'project_name': "Movies App",
        'title': "Details",
        'details': data,
    }
    return render(request, "baseapp/details.html", context=context)


def add_movies(request):
    if request.method == 'POST':
        film_name = request.POST.get('moviename')
        desc = request.POST.get('moviestory')
        rel_year = request.POST.get('releaseyear')
        rel_year = datetime.strptime(rel_year, '%Y-%m-%d').date().year
        image = request.FILES['posterimage']
        res = Movies(name=film_name, description=desc, year=rel_year, poster=image)
        res.save()
        messages.info(request, "Data saved")
        return redirect('/')
    else:
        context = {
            'project_name': "Movies App",
            'title': "Add movies",
        }
        return render(request, 'baseapp/add.html', context=context)


def update(request, pk):
    instance = Movies.objects.get(pk=pk)
    form = MoviesForm(request.POST or None, request.FILES, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        form = MoviesForm(instance=instance)
        context = {
            'project_name': "Movies App",
            'title': "Update Details",
            'form': form,
            'instance': instance
        }
        return render(request, "baseapp/edit.html", context=context)


def delete(request, pk):
    if request.method == 'POST':
        movie = Movies.objects.get(pk=pk)
        movie.delete()
        return redirect('/')
    else:
        context = {
            'project_name': "Movies App",
            'title': "Delete",
        }
        return render(request, "baseapp/delete.html", context=context)
