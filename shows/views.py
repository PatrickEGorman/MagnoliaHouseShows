from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import datetime

from shows.serializers import ShowSerializer
from .models import Show


def past_shows(request):
    return render(request, 'past_shows.html', {})


def view_show(request, show_id):
    return render(request, 'view_show.html', {'show_id': show_id})


def get_show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    serializer = ShowSerializer(show)
    return JsonResponse(serializer.data, safe=False)


def get_shows_list(request):
    num_shows = 11
    if request.GET.get('num_shows'):
        num_shows = int(request.GET.get('num_shows'))
    past_shows = False
    if request.GET.get('past_shows'):
        past_shows = request.GET.get('past_shows')
    show_list = Show.objects.all()
    date = datetime.datetime.now().date()
    if past_shows == "True" or past_shows == "true":
        show_list = show_list.filter(date__lte=date).order_by('date').reverse()[:num_shows]
    else:
        show_list = show_list.filter(date__gte=date).order_by('date')[:num_shows]
    serializer = ShowSerializer(show_list, many=True)
    return JsonResponse(serializer.data, safe=False)
