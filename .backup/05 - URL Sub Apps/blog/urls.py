from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # ini views yang ada didalam folder blog
    path('recent/', views.recent, name='recent')
]
