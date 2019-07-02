from django.shortcuts import render


def fliers(request):
    return render(request, 'fliers.html', {})


def photos(request):
    return render(request, 'photos.html', {})


def videos(request):
    return render(request, 'videos.html', {})