from django.views import View
from django.urls import path
from shows import views

urlpatterns = [
    path("moviesList", views.MoviesListView.as_view(), name="Movies List"),
    path("singleMovie/<pk>", views.SingleMovieView.as_view(), name=" Single Movie"),
    path("playsList", views.PlaysListView.as_view(), name="Plays List"),
    path("singlePlay/<pk>", views.SinglePlayView.as_view(), name="Single Play")
]