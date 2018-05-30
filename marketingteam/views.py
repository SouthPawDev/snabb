from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from marketingteam import models
# Create your views here.


class SmrListView(ListView):
    context_object_name = 'marketingteam'
    model = models.Smr


class SmrDetailView(DetailView):
    context_object_name = 'marketingteam_detail'
    model = models.Smr


class SmrCreateView(CreateView):
    fields = ('smr_pic', 'first_name', 'last_name', 'phone_number', 'smr_franchise', 'smr_car')
    model = models.Smr


class SmrUpdateView(UpdateView):
    fields = ('smr_pic', 'first_name', 'last_name', 'phone_number', 'smr_franchise', 'smr_car')
    model = models.Smr


class SmrDeleteView(DeleteView):
    model = models.Smr
    success_url = reverse_lazy('marketingteam:list')
