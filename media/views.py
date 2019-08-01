import datetime

from django.urls import reverse_lazy

from .forms import PhotoSubmitForm, VideoSubmitForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from .serializers import FlierSerializer, PhotoSerializer, YoutubeSerializer
from .models import Flier, Photo, YoutubeVideo



def fliers(request):
    return render(request, 'fliers.html', {})


def photos(request):
    return render(request, 'photos.html', {})


def videos(request):
    return render(request, 'videos.html', {})


def get_fliers_list(request):
    num_fliers = 11
    if request.GET.get('num_fliers'):
        num_fliers = int(request.GET.get('num_fliers'))
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
    num_photos = 11
    if request.GET.get('num_photos'):
        num_photos = int(request.GET.get('num_photos'))
    photo_list = Photo.objects.all()
    photo_list = photo_list[:num_photos]
    serializer = PhotoSerializer(photo_list, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_videos_list(request):
    num_videos = 11
    if request.GET.get('num_videos'):
        num_videos = int(request.GET.get('num_videos'))
    video_list = YoutubeVideo.objects.all()
    video_list = video_list[:num_videos]
    serializer = YoutubeSerializer(video_list, many=True)
    return JsonResponse(serializer.data, safe=False)


class SubmitPhoto(LoginRequiredMixin, generic.CreateView):
    form_class = PhotoSubmitForm
    success_url = reverse_lazy('photos')
    template_name = 'photo_form_page.html'

    def form_valid(self, form):
        form.instance.metaData.posted_by = self.request.user
        return super().form_valid(form)


class SubmitVideo(LoginRequiredMixin, generic.CreateView):
    form_class = VideoSubmitForm
    success_url = reverse_lazy('videos')
    template_name = 'video_form_page.html'

    def form_valid(self, form):
        form.instance.metaData.posted_by = self.request.user
        return super().form_valid(form)
