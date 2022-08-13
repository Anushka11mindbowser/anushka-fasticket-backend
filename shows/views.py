from rest_framework.response import Response
from rest_framework import status
from .models import (
                    Movies,
                    Plays
                    )
from .serializers import (
                        MovieSerializer,
                        PlaysSerializer
                        )
from rest_framework.generics import (
                                    ListAPIView,
                                    RetrieveAPIView
                                    )
# Create your views here.

class MoviesListView(ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = []

    def get_queryset(self):
       movies = Movies.objects.all()
       return movies

    def get(self, request, *args, **kwargs):
        movies = self.get_queryset()
        serializer = self.serializer_class(movies, many=True)
        response = {
            "message":"List of Movies",
            "data":serializer.data
                    }
        return Response(response, status=status.HTTP_200_OK)
    
class SingleMovieView(RetrieveAPIView):
    serializer_class = MovieSerializer
    permission_classes = []

    def get_object(self,pk):
        return Movies.objects.get(pk=pk)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        movie = self.get_object(pk)
        serializer = self.serializer_class(movie, many=False)
        response = {
            "message":"Single Movie",
            "data" : serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)


class PlaysListView(ListAPIView):
    serializer_class = PlaysSerializer
    permission_classes = []

    def get_queryset(self):
        plays = Plays.objects.all()
        return plays

    def get(self, request, *args, **kwargs):
        plays = self.get_queryset()
        serializer = self.serializer_class(plays, many=True)
        response = {
            "message":"List of Plays",
            "data":serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)


class SinglePlayView(RetrieveAPIView):
    serializer_class = PlaysSerializer
    permission_classes = []

    def get_object(self,pk):
        return Plays.objects.get(pk=pk)
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        play = self.get_object(pk)
        serializer = self.serializer_class(play, many=False)
        response = {
            "message":"Single Play",
            "data":serializer.data
                    }
        return Response(response, status=status.HTTP_200_OK)

       
       
        

