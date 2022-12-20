from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


@api_view(['GET'])
def test(request):
    return Response({'message':'hello world'}, 200)

@api_view(['GET'])
def movies(request):
    queryset = Movie.objects.all()
    serializer = MovieSerializer(queryset)
    return Response(serializer, status=201)

@api_view(['GET'])
def show_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    average_rating = movie.average_rating
    serializer = MovieSerializer(movie)
    return Response(serializer)
    
# @api_view(['POST'])
# def post_movie(request, )