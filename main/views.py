from main.modules import youtube
from main.models import Movie, News, OldNews, Work, OldWork, Essay
from django.shortcuts import render


#メインページ
def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def news(request):
    news = News.objects.all().order_by('created_at').reverse()
    old_news = OldNews.objects.all().order_by('created_at').reverse()
    context = {"news": news, "old_news": old_news}
    return render(request, "main/news.html", context)

def work(request):
    works = Work.objects.all().order_by('created_at').reverse()
    old_works = OldWork.objects.all().order_by('created_at').reverse()
    context = {"works": works, "old_works": old_works}
    return render(request, "main/work.html", context)

def essay(request):
    essaies = Essay.objects.all().order_by('id').reverse()
    context = {"essaies": essaies}
    return render(request, "main/essay.html", context)

def movie(request):
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, "main/movie.html", context)

def contact(request):
    return render(request, "main/contact.html")

def manage(request):
    if request.method == "POST":
        youtube_movies = youtube.get_youtube()
        for movie in youtube_movies:
            if not Movie.objects.filter(movie_id=movie[2]).exists():
                Movie.objects.create(created_at=movie[0], title=movie[1], movie_id=movie[2])
    return render(request, "main/manage.html")

def exhibition1(request):
    return render(request, "main/exhibition1.html")


#第1回松本家展
def guide(request):
    return render(request, "main/exhibition1/guide.html")

def model(request):
    return render(request, "main/exhibition1/model.html")

def virtual(request):
    return render(request, "main/exhibition1/virtual.html")

def session(request):
    return render(request, "main/exhibition1/session.html")

def movie2(request):
    return render(request, "main/exhibition1/movie2.html")

def essay2(request):
    return render(request, "main/exhibition1/essay2.html")

def photo(request):
    return render(request, "main/exhibition1/photo.html")


#松本家通信2021年夏季号
def introduction(request):
    return render(request, "main/exhibition1/essay/introduction.html")

def essay_ci(request):
    return render(request, "main/exhibition1/essay/essay-ci.html")

def essay_hi(request):
    return render(request, "main/exhibition1/essay/essay-hi.html")

def essay_ys(request):
    return render(request, "main/exhibition1/essay/essay-ys.html")

def essay_rs(request):
    return render(request, "main/exhibition1/essay/essay-rs.html")

def essay_th(request):
    return render(request, "main/exhibition1/essay/essay-th.html")

def essay_ah(request):
    return render(request, "main/exhibition1/essay/essay-ah.html")

def essay_kh(request):
    return render(request, "main/exhibition1/essay/essay-kh.html")

def essay_hy(request):
    return render(request, "main/exhibition1/essay/essay-hy.html")

def essay_tm(request):
    return render(request, "main/exhibition1/essay/essay-tm.html")

def editors_note(request):
    return render(request, "main/exhibition1/essay/editors-note.html")
