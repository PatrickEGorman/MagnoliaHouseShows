from django.shortcuts import render

from info.models import History


def about(request):
    return render(request, 'about.html', {})


def directions(request):
    return render(request, 'directions.html', {})


def history_list(request):
    histories = History.objects.all()
    return render(request, 'history.html', {'histories': histories})


def view_history(request, history_id):
    history = History.objects.get(id=history_id)
    return render(request, 'view_history.html', {'history': history})


def contact(request):
    return render(request, 'contact.html', {})
