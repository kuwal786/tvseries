from django.db import models

class Genre(models.Model):
    Name=models.CharField(max_length=100)
    n=models.IntegerField()
    def __str__(self):
        return self.Name


class Anime(models.Model):
    anime_id=models.IntegerField()
    name = models.CharField(max_length=200)
    genres=models.ManyToManyField(Genre)
    tag=models.CharField(max_length=1000)
    epidodes=models.IntegerField()
    rating=models.DecimalField(decimal_places=1,max_digits=2)
    members=models.IntegerField()
    def __str__ (self):
         return self.name+str(self.genres)
