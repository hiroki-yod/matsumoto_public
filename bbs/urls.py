from django.urls import path
from bbs import views

app_name = "bbs"

urlpatterns = [
    path('', views.secret, name="secret"),
    path('<int:post_id>/', views.post_detail, name="post_detail"),
]
