from django.views.generic import ListView, DetailView
from .models import Snack


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

    # if you add code below then templates can use things vs. object_list
    # context_object_name = "things"


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack