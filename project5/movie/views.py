from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }

    return render(request, 'index.html', context)


def detail(request, movie_id):
    mov = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'info': mov})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dir = request.POST.get('dir')
        year = request.POST.get('year')
        Imdb = request.POST.get('Imdb')
        img = request.FILES['img']
        movie = Movie(name=name, dir=dir, year=year, Imdb=Imdb, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, update_id):
    movie = Movie.objects.get(id=update_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete(request, delete_id):
    if request.method=="POST":
        movie=Movie.objects.get(id=delete_id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')

