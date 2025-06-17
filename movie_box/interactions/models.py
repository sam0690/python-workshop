from django.db import models
# from users.models import User
from movies.models import Movie
from django.contrib.auth.models import User 

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(help_text="Rating score from 1 to 5")
    rated_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = ('user', 'movie')  # Ensure a user can only rate a movie once

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.score})"

class watchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    class Meta:
        verbose_name = 'Watch History'
        verbose_name_plural = 'Watch Histories'
        unique_together = ('user', 'movie')  # Ensure a user can only have one entry per movie

    def __str__(self):
        return f"{self.user.username} watched {self.movie.title} on {self.watched_at}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        unique_together = ('user', 'movie')  # Ensure a user can only favorite a movie once

    def __str__(self):
        return f"{self.user.username} favorited {self.movie.title}"