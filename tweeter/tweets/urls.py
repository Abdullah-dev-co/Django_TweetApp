# tweets/urls.py
from django.urls import path
from .views import (
    home,
    register,
    user_login,
    user_logout,
    TweetUpdateView,
    TweetDeleteView
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('tweet/<int:pk>/update/', TweetUpdateView.as_view(), name='tweet-update'),
    path('tweet/<int:pk>/delete/', TweetDeleteView.as_view(), name='tweet-delete'),
]