from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Movie,Review
from django.db.models import Count

def index(request):
    if request.method == "GET":
        movie = Movie.objects.all().order_by("-reg_date")
        if 'order' in request.GET :
            movie = movie.annotate(count_review = Count('review')).order_by('-count_review')
        return render(request,"exam/index.html",{'movie':movie})
    else:
        genre = request.POST['genre']
        movie = Movie.objects.filter(genre = genre)
        return render(request,"exam/index.html",{'movie':movie})


def movie_add(request):
    if request.method == "GET":
        return render(request,'exam/movie_add.html')
    else:
        Movie.objects.create(
            genre = request.POST['genre'],
            movie_name = request.POST['movie_name'],
            movie_summary = request.POST['movie_summary']
        )
        return redirect("/")
    

def info(request,id):
    movie = Movie.objects.get(id=id)
    review = movie.review_set.all()
    context = {
        'movie' : movie,
        'review' : review.order_by('-reg_date')
        }
    return render(request,"exam/info.html",context)

def review_add(request,id):
    reviewer_name = request.POST['reviewer_name']
    if reviewer_name == '':
        Review.objects.create(
            movie = Movie.objects.get(id=id),
            review_text = request.POST['review_text'],
            score = request.POST['score']
        )
    else:
        Review.objects.create(
            movie = Movie.objects.get(id=id),
            reviewer_name = reviewer_name,
            review_text = request.POST['review_text'],
            score = request.POST['score']
        )
    return HttpResponse(status=200)

def load_review(request,id):
    movie = Movie.objects.get(id=id)
    review = movie.review_set.all()
    review_list_sum = [i.score for i in review]
    reviews_score = sum(review_list_sum) / len(review_list_sum) if len(review_list_sum) != 0  else 0

    review_list_order = movie.review_set.all().order_by('-reg_date')
    review_list = []
    for i in review_list_order:
        review = {
            'reg_date': i.reg_date,
            'reviewer_name': i.reviewer_name,
            'review_text': i.review_text,
            'score': i.score
        }
        review_list.append(review)
    
    context = {'review_list': review_list,'reviews_score':reviews_score}

    return JsonResponse(context)

def movie_update(request,id):
    movie = Movie.objects.get(id=id)
    if request.method == "GET" :
        return render(request,'exam/movie_update.html',{'movie':movie})
    else :
        movie.genre = request.POST['genre']
        movie.movie_name = request.POST['movie_name']
        movie.movie_summary = request.POST['movie_summary']
        movie.save()
        return redirect("/")
    
def movie_delete(request,id):
    Movie.objects.get(id=id).delete()
    return redirect("/")
