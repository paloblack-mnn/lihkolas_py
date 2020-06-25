from .models import Pages,Gallery

def base(request):
    gallery = Gallery.objects.filter(public=1)
    return {'gallery':gallery}
