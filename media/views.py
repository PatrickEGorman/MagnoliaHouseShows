import datetime

from django.http import JsonResponse
from django.shortcuts import render
from .serializers import FlierSerializer, PhotoSerializer, YoutubeSerializer
from .models import Flier, Photo, YoutubeVideo



def fliers(request):
    return render(request, 'fliers.html', {})


def photos(request):
    return render(request, 'photos.html', {})


def videos(request):
    return render(request, 'videos.html', {})


def get_fliers_list(request):
    num_fliers = 10
    if request.GET.get('num_fliers'):
        num_fliers = request.GET.get('num_fliers')
    past_shows = False
    if request.GET.get('past_shows'):
        past_shows = request.GET.get('past_shows')
    flier_list = Flier.objects.all()
    date = datetime.datetime.now().date()
    if past_shows == "True" or past_shows == "true":
        flier_list = flier_list.filter(date__lte=date).order_by('date').reverse()[:num_fliers]
    else:
        flier_list = flier_list.filter(date__gte=date).order_by('date')[:num_fliers]
    serializer = FlierSerializer(flier_list, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_photos_list(request):
    num_photos = 10
    if request.GET.get('num_photos'):
        num_photos = request.GET.get('num_photos')
    photo_list = Photo.objects.all()
    photo_list = photo_list[:num_photos]
    serializer = PhotoSerializer(photo_list, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_videos_list(request):
    num_videos = 10
    if request.GET.get('num_videos'):
        num_videos = request.GET.get('num_videos')
    video_list = YoutubeVideo.objects.all()
    video_list = video_list[:num_videos]
    serializer = YoutubeSerializer(video_list, many=True)
    return JsonResponse(serializer.data, safe=False)