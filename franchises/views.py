from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from franchises import models
# Create your views here.


class FranchiseListView(ListView):
    context_object_name = 'franchises'
    model = models.Franchise


class FranchiseDetailView(DetailView):
    context_object_name = 'franchise_detail'
    model = models.Franchise


class FranchiseCreateView(CreateView):
    fields = ('name', 'location', 'phone_number')
    model = models.Franchise


class FranchiseUpdateView(UpdateView):
    fields = ('phone_number',)
    model = models.Franchise


class FranchiseDeleteView(DeleteView):
    model = models.Franchise
    success_url = reverse_lazy('franchises:list')
