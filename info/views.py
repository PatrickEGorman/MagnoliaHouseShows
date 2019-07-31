from django.shortcuts import render

from info.models import History


def about(request):
    return render(request, 'about.html', {})


def directions(request):
    return render(request, 'directions.html', {})


def history(request):
    histories = History.objects.all()
    return render(request, 'history.html', {'histories': histories})


def contact(request):
    return render(request, 'contact.html', {})
