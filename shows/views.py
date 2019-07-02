from django.shortcuts import render
from django.http import JsonResponse
import datetime

from shows.serializers import ShowSerializer
from .models import Show


def shows(request):
    return render(request, 'shows.html', {})


def view_show(request):
    return render(request, 'view_show.html', {})


def get_shows_list(request):
    num_shows = 5
    if request.GET.get('num_shows'):
        num_shows = request.GET.get('num_shows')
    past_shows = False
    if request.GET.get('past_shows'):
        past_shows = request.GET.get('past_shows')
    show_list = Show.objects.all()
    date = datetime.datetime.now().date()
    if past_shows:
        show_list = show_list.filter(date__lte=date).order_by('date').reverse()[:num_shows]
    else:
        show_list = show_list.filter(date__gte=date).order_by('date')[:num_shows]
    serializer = ShowSerializer(show_list, many=True)
    return JsonResponse(serializer.data, safe=False)
