from django.db import models

# Create your models here.
# class Movie(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=255)
#     release_year = models.IntegerField()
#     rating = models.DecimalField(max_digits=3, decimal_places=1,max_length=4)


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=255)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return  self.title
    