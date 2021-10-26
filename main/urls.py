from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('news/', views.news, name="news"),
    path('work/', views.work, name="work"),
    path('essay/', views.essay, name="essay"),
    path('movie/', views.movie, name="movie"),
    path('contact/', views.contact, name="contact"),
    path('manage/', views.manage, name="manage"),

    #松本家通信2021年夏季号のQRコード維持のため.htmlを付ける
    path('exhibition1.html/', views.exhibition1, name="exhibition1"),
    path('exhibition-first/guide.html/', views.guide, name="guide"),
    path('exhibition-first/model.html/', views.model, name="model"),
    path('exhibition-first/virtual.html/', views.virtual, name="virtual"),
    path('exhibition-first/photo.html/', views.photo, name="photo"),
    path('exhibition-first/session.html/', views.session, name="session"),
    path('exhibition-first/movie.html/', views.movie2, name="movie2"),
    path('exhibition-first/essay.html/', views.essay2, name="essay2"),
    path('exhibition-first/essay/introduction.html/', views.introduction, name="introduction"),
    path('exhibition-first/essay/essay-ci.html/', views.essay_ci, name="essay-ci"),
    path('exhibition-first/essay/essay-hi.html/', views.essay_hi, name="essay-hi"),
    path('exhibition-first/essay/essay-ys.html/', views.essay_ys, name="essay-ys"),
    path('exhibition-first/essay/essay-rs.html/', views.essay_rs, name="essay-rs"),
    path('exhibition-first/essay/essay-th.html/', views.essay_th, name="essay-th"),
    path('exhibition-first/essay/essay-ah.html/', views.essay_ah, name="essay-ah"),
    path('exhibition-first/essay/essay-kh.html/', views.essay_kh, name="essay-kh"),
    path('exhibition-first/essay/essay-hy.html/', views.essay_hy, name="essay-hy"),
    path('exhibition-first/essay/essay-tm.html/', views.essay_tm, name="essay-tm"),
    path('exhibition-first/essay/editors-note.html/', views.editors_note, name="editors-note"),
]