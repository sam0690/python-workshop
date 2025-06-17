from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    
class Movie(models.Model):
    language_Choices = [
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Spanish', 'Spanish'),
        ('French', 'French'),
        ('German', 'German'),
        ('Chinese', 'Chinese'),
        ('Japanese', 'Japanese'),
        ('Korean', 'Korean'),
        ('Other', 'Other')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.DateField()
    duration = models.PositiveIntegerField()
    language = models.CharField(max_length=50, choices=language_Choices, default='English')
    cover_image = models.URLField(max_length=200, help_text="URL of the movie cover image", null=True, blank=True)
    trailer_url = models.URLField(max_length=200, help_text="URL of the movie trailer" , null=True, blank=True)
    video_url = models.URLField(max_length=200, help_text="URL of the movie video",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    is_trending = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    
