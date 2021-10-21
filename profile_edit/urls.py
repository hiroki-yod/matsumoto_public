from django.urls import path
from profile_edit import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "profile_edit"

urlpatterns = [
    path('accounts/signup/profile/new/', views.profile_new, name="profile_new"),
    path('profile/<int:profile_id>/', views.profile_edit, name="profile_edit"),
    path('notice/<int:profile_id>/', views.notice, name="notice"),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)