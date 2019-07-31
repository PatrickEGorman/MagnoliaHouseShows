from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Artist, Genre
from .serializers import ArtistSerializer, GenreSerializer


def music(request):
    return render(request, 'music.html', {})


def view_album(request):
    return render(request, 'view_album.html', {})


def view_artist(request, artist_id):
    return render(request, 'view_artist.html', {'artist_id': artist_id})


def get_artist(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistSerializer(artist)
    return JsonResponse(serializer.data, safe=False)


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
    if request.GET.get('Embed'):
        embed = request.GET.get('Embed')
        if embed == "bandcamp":
            artist_list = artist_list.exclude(bandcamp_embed_code='')
        elif embed == "soundcloud":
            artist_list = artist_list.exclude(soundcloud_embed_code='')
        elif embed == "youtube":
            artist_list = artist_list.exclude(youtube_embed_code='')
    artist_list = artist_list.distinct()
    serializer = ArtistSerializer(artist_list, many=True)
    return JsonResponse(serializer.data, safe=False)


def list_genres(request):
    return render(request, 'list_genres.html', {})


def get_genre_list(request):
    genre_list = Genre.objects.all()
    serializer = GenreSerializer(genre_list, many=True)
    return JsonResponse(serializer.data, safe=False)
