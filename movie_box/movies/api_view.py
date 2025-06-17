from movies.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404

@api_view(["GET", "POST"])
def get_movies(request):
   

    if(request.method == "POST"):    
        # Handle POST request if needed
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response({"message": "Movie added successfully"}, status=201)
    else:
        pass
   
    movie_object = Movie.objects.all()
    movies = MovieSerializer(movie_object, many=True)
    return Response(movies.data)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail_view(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=404)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  
        return Response(serializer.errors, status=400)

    elif request.method == "DELETE":
        movie.delete()
        return Response(status=204)  # No content 