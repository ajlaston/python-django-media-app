from django.db import models
from movies.models import Genre, Movie, Serie
from tastypie.resources import ModelResource, fields, ALL


# Create your models here.

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        ordering: ['release_year', 'title', 'price']
        filtering = {
            'release_year' : ALL,
            'price' : ALL,
            'title' : ALL,
            'in_stock' : ALL
        }
        

class GenreResource(ModelResource):
    class Meta: 
        queryset = Genre.objects.all()
        resource_name = 'genres'

