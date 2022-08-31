from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView,
from django.urls import reverse_lazy
from .models import Snack

# Views for different functionality create update and delete aka CRUD

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

    # if you add code below then templates can use things vs. object_list
    # context_object_name = "things"

class SnackCreateView(CreateView):
    model = Snack
    template_name = "snack_create.html"
    fields = ['name','purchaser', 'description']

class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ['name','purchaser', 'description']

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

class SnackDeleteView(DeleteView)
    model = Snack
    template_name = "snack_delete.html"
    success_url = reverse_lazy('snack_list')