
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

data = {
    'movies': [
        {
            'id' : 8,
            "title" : "Avengers",
            "year" : 2008
        },
        {
            'id' : 9,
            "title" : "Iron Man 3",
            "year" : 2010
        },
        {
            'id' : 10,
            "title" : "Avengers EndGame",
            "year" : 2021
        }
    ]
}


def home(request):
    return HttpResponse("This is a Home Page")

def movies(request):
    data = Movie.objects.all()
    return render(request,"movies/movies.html",{'movies' : data})

def detail(request,id):
    data = Movie.objects.get(pk=id)
    return render(request,"movies/detail.html",{'movies':data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title,year = year)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request,"movies/add.html")

def delete(request,id):
    Movie.objects.get(pk=id).delete()
    return HttpResponseRedirect('/movies')