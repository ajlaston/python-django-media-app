from django.db import models

# Create your models here.
"""
    field:
        char (string)
        int
        float
        boolean
"""
class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Movie(models.Model):
    
    title = models.CharField(max_length=250)
    release_year = models.IntegerField()
    in_stock = models.FloatField()
    price = models.FloatField()
    duration_min = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    

    def __str__(self):
        return  str(self.release_year) + " | " + self.title

class Serie(models.Model):

    class Meta:
        verbose_name_plural = 'Series'

    title = models.CharField(max_length=250)
    seasons = models.IntegerField()
    episodes = models.IntegerField()
    release_year = models.IntegerField()
    in_stock = models.FloatField()
    price = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)