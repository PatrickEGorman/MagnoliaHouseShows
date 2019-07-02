from django.shortcuts import render


def music(request):
    return render(request, 'music.html', {})


def view_album(request):
    return render(request, 'view_album.html', {})


def view_band(request):
    return render(request, 'view_band.html', {})