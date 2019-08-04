from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from info.forms import HistoryForm
from info.models import History


def show_about(request):
    return render(request, 'about.html', {})


def list_directions(request):
    return render(request, 'directions.html', {})


def history_list(request):
    histories = History.objects.all()
    return render(request, 'history.html', {'histories': histories})


def view_history(request, history_id):
    history = History.objects.get(id=history_id)
    return render(request, 'view_history.html', {'history': history})


def list_contacts(request):
    return render(request, 'contact.html', {})


class CreateHistory(LoginRequiredMixin, generic.CreateView):
    form_class = HistoryForm
    success_url = reverse_lazy('history')
    template_name = 'history_form_page.html'

    def form_valid(self, form):
        form.instance.metaData.posted_by = self.request.user
        return super().form_valid(form)

