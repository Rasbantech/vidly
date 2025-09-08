from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Movies, Genre  

# Create your views here.
def index(request):
    movies = Movies.objects.all()
    return render(request, "movies/index.html", {"movies": movies})


def details(request, id):
    movie =get_object_or_404(Movies,pk=id)
    return render(request, "movies/details.html", {"movie":movie})

    