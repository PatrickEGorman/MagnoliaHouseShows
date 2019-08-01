from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from info.forms import HistoryForm
from info.models import InfoPage, Directions, History


def show_about(request):
    about = InfoPage.objects.filter(page_name="about")
    return render(request, 'about.html', {'about': about})


def list_directions(request):
    directions = Directions.objects.all()
    return render(request, 'directions.html', {'directions': directions})


def history_list(request):
    histories = History.objects.all()
    return render(request, 'history.html', {'histories': histories})


def view_history(request, history_id):
    history = History.objects.get(id=history_id)
    return render(request, 'view_history.html', {'history': history})


def list_contacts(request):
    contacts = InfoPage.objects.filter(page_name="contact")
    return render(request, 'contact.html', {'contacts': contacts})


class CreateHistory(generic.CreateView):
    form_class = HistoryForm
    success_url = reverse_lazy('history')
    template_name = 'history_form_page.html'

