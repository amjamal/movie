from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    dir = models.CharField(max_length=50)
    year = models.IntegerField()
    Imdb = models.FloatField()
    img = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.name
