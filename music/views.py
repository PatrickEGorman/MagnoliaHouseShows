from django.http import JsonResponse
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer


def music(request):
    return render(request, 'music.html', {})


def view_album(request):
    return render(request, 'view_album.html', {})


def view_band(request):
    return render(request, 'view_band.html', {})


def get_artist_list(request):
    num_artists = 10
    if request.GET.get('num_artists'):
        num_artists = int(request.GET.get('num_artists'))
    artist_list = Artist.objects.all()[:num_artists]
    serializer = ArtistSerializer(artist_list, many=True)
    return JsonResponse(serializer.data, safe=False)