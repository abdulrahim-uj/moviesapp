from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    year = models.IntegerField()
    poster = models.ImageField(upload_to="movies/posters/")

    def __str__(self):
        return self.name
