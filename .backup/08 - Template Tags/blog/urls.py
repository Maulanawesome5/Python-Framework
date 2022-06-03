from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ini views yang ada didalam folder blog
    path('cerita/', views.cerita, name='cerita'),
    path('news/', views.news, name='news')
]
