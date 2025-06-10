from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100, blank=True, default="noname")
    image_url = models.URLField(max_length=200) 

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Viewers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    author = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    image = models.OneToOneField(Image, on_delete=models.CASCADE, null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    Viewers = models.ManyToManyField(Viewers, blank=True , null=True)

    def __str__(self):
        return self.title
    









class Members(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name