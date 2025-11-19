from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse    
from .serializers import MovieSerializer  
from rest_framework.response import Response
from rest_framework.decorators import api_view  
# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     movie_data = {
#         'movies': list(movies.values())
#     }
#     return JsonResponse(movie_data, safe=False)


# def movie_detail(request, pk):
#     try:
#        movie = Movie.objects.get(pk=pk)
#        movie_data = {
#             "name": movie.name,
#             "description": movie.description,
#             "release_year": movie.release_year,
#             "rating": movie.rating
#         }
#     except Movie.DoesNotExist:
#         movie_data = {"error": "Movie not found"}   
#     return JsonResponse(movie_data)

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
    #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            # Normally, you would save the data to the database here.
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)
        #return JsonResponse(serializer.data) 
        return Response(serializer.data)
    
    if request.method == 'PUT':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)
        
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)
        
        movie.delete()
        return Response(status=204)
    
