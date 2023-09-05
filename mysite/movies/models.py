from django.db import models

# Create your models here.
class MoviesData(models.Model):
    name = models.CharField(max_length=200)
    duration  = models.FloatField()
    rating = models.FloatField()
    types = models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to='Images/', default='Image/None/Noimg.jpg')

    def __str__(self) -> str:
        return self.name
