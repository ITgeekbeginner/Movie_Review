from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
   username =  models.CharField(max_length=200)
   email = models.EmailField(max_length=254)
   password = models.CharField(max_length=8)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.email
   
class Genre(models.Model):
   name = models.CharField(max_length=20)

   def __str__(self):
      return self.name
   
class Movie(models.Model):
   title = models.CharField(max_length=200)
   genre = models.ManyToManyField(Genre)
   director = models.CharField(max_length=50)
   realese_year = models.DateField(auto_created=False)
   description = models.TextField(max_length=500)
   average_rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=False)

   def __str__(self):
      return self.title
   
class Review(models.Model):
   movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   review = models.TextField(max_length=500)
   created_at = models.DateField(auto_now_add=True)

   def __str__(self):
      return f'Reviewed by {self.user_id.username} for {self.movie_id.title}'


# Create your models here.
