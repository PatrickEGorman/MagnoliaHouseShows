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
    artist_list = Artist.objects.all()
    if request.GET.get('Genre'):
        artist_list = artist_list.filter(genres__id=request.GET.get('Genre'))
    if request.GET.get('Hometown'):
        artist_list = artist_list.filter(hometown=request.GET.get('Hometown'))
    if request.GET.get('Social'):
        social = request.GET.get('Social')
        if social == "facebook":
            artist_list = artist_list.exclude(facebook='')
        elif social == "bandcamp":
            artist_list = artist_list.exclude(bandcamp='', bandcamp_embed_code='')
        elif social == "soundcloud":
            artist_list = artist_list.exclude(soundcloud='', soundcloud_embed_code='')
        elif social == "youtube":
            artist_list = artist_list.exclude(youtube='', youtube_embed_code='')
    artist_list = artist_list.distinct()
    serializer = ArtistSerializer(artist_list, many=True)
    return JsonResponse(serializer.data, safe=False)