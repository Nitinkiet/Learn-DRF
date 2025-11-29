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
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,null=True,related_name="watchlist")

    def __str__(self):
        return  self.title 
    

class Review(models.Model):
    review_user = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    description = models.TextField(max_length=200,null=True)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name="reviews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.rating} - {self.watchlist.title}"
    

    