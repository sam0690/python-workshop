from .models import Genre

def genres(request):
    data = {
        "genres": Genre.objects.all()
    }
    return data

  