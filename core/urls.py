from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('berita/', views.news_list, name='news_list'),
    path('berita/<slug:slug>/', views.news_detail, name='news_detail'),
]
