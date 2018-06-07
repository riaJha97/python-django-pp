from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MovieForm, CinemaForm
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'test/home.html')


def book_movie(request):
    if request.method == 'GET':
        return render(request, 'test/movie_form.html')
    else:
        pass


def available_cinemas(request, movie_name=""):
    if request.method == 'GET':
        return render(request, 'test/cinema_form.html', {'cinema_form': CinemaForm(movie_name=movie_name)})
    else:
        return HttpResponse("Success!")
