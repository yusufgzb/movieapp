from datetime import date
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect,HttpResponse
from .form import ComentForm
from django.urls import reverse
from .models import Movie, Slider



# Anasayfa
def index(request):
    #is_active=True,is_home=True olanları aliyoruz
    movies = Movie.objects.filter(is_active=True,is_home=True)
    #anasayfadaki kayan film yapısı
    sliders = Slider.objects.filter(is_active=True)
    return render(request, 'movies/index.html', {
        "movies": movies,
        "sliders": sliders
    })

#film sayfası
def movies(request):
    # is_active=True olanları alıyoruz
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'movies/movies.html', {
        "movies": movies
    })

#film detay sayfası
def movie_details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    #ayrıntı sayfasında yorum yapmak için CommentFormu gönderdik
    comment_form = ComentForm()
    #html içinden bit post isteği gelirse yorumu db ye kayı edecek
    if request.method == "POST":
        comment_form=ComentForm(request.POST)
        #gelen yorumda Modelde belirttiğimiz kurallara uygun olup olmadığına bakıyoruz
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.save()
            #aynı fiminin detayına gidiyoruz
            return HttpResponseRedirect(reverse("movie_details",args=[slug]))


    return render(request, 'movies/movie-details.html', {
        "movie": movie,
        "genres": movie.genres.all(),
        "people": movie.people.all(),
        "videos": movie.video_set.all(),
        "comments":movie.comments.all(),
        "comment_form":comment_form
})

def events(request):
    return render(request,"bos-sayfa.html")

def people(request):

    return render(request,"movies/base.html")

def sport(request):
    return render(request,"bos-sayfa.html")



