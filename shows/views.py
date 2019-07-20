from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import datetime

from shows.serializers import ShowSerializer
from .models import Show
from main.util import months


def past_shows(request):
    return render(request, 'past_shows.html', {})


def view_show(request, show_id):
    return render(request, 'view_show.html', {'show_id': show_id})


def get_show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    serializer = ShowSerializer(show)
    return JsonResponse(serializer.data, safe=False)


def get_shows_list(request):
    past = False
    if request.GET.get('past_shows'):
        past = request.GET.get('past_shows')
    show_list = Show.objects.all()
    date = datetime.datetime.now().date()
    if past == "True" or past == "true":
        show_list = show_list.filter(date__lte=date).order_by('date').reverse()
    else:
        show_list = show_list.filter(date__gte=date).order_by('date')
    if request.GET.get('Date'):
        date = request.GET.get('Date')
        split_date = date.split("-")
        year = int(split_date[0])
        month = int(split_date[1])
        show_list = show_list.filter(date__year=year, date__month=month)
    if request.GET.get('Genre'):
        show_list = show_list.filter(artists__genres__id=request.GET.get('Genre'))
    if request.GET.get('Artist'):
        show_list = show_list.filter(artists__id=request.GET.get('Artist'))
    serializer = ShowSerializer(show_list, many=True)
    return JsonResponse(serializer.data, safe=False)
