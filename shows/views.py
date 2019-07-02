from django.shortcuts import render


def shows(request):
    return render(request, 'shows.html', {})


def view_show(request):
    return render(request, 'view_show.html', {})
