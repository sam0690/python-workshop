from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100) # Name of the profile
    bio = models.TextField()  # Short biography or description 
    location = models.CharField(max_length=100, blank=True, null=True)  # Location of the user  
    website = models.URLField(blank=True, null=True)  # Personal or professional website
    social_links = models.JSONField(blank=True, null=True)  # Links to social media profiles (e.g., Twitter, LinkedIn)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the profile was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the profile was last updated
    is_active = models.BooleanField(default=True)  # Whether the profile is active or not