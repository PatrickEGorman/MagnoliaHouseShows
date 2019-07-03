from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {})


def directions(request):
    return render(request, 'directions.html', {})


def event_calendar(request):
    return render(request, 'event_calendar.html', {})


def history(request):
    return render(request, 'history.html', {})


def contact(request):
    return render(request, 'contact.html', {})
