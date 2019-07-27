from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {})


def directions(request):
    return render(request, 'directions.html', {})


def history(request):
    return render(request, 'history.html', {})


def contact(request):
    return render(request, 'contact.html', {})
