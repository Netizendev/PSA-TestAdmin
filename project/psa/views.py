from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy

from .models import Provsvar, Patient, Hantera

def index(request):
    pass

def detail(request):
    pass


class IndexView(generic.ListView):
    template_name = 'psa/index.html'
    context_object_name = 'latest_provsvar_list'

    def get_queryset(self):
        """Visar de tio senaste provsvaren."""
        return Provsvar.objects.order_by('-created')[:10]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['hantera_list'] = Hantera.objects.all()
        return context

        
# class DetailView(generic.DetailView):
#     model = Provsvar
#     template_name = 'psa/detail.html'


class ProvsvarDetail(generic.DetailView):
    model = Provsvar
    template_name = 'psa/detail.html'

class HanteraDetail(generic.DetailView):
    model = Hantera
    template_name = 'psa/prov.html'


class ProvsvarCreateView(generic.CreateView):
    model = Provsvar
    fields = ['ssn', 'result']
    template_name = 'psa/add_provsvar.html'
    success_url = '../'
    # success_message = "%(ssn)s was created successfully"

class PatientCreateView(generic.CreateView):
    model = Patient
    fields = ['ssn', 'namn','gata','postort', 'postnr', 'mail','operationsdatum']
    template_name = 'psa/add_patient.html'
    success_url = '../'
    # success_message = "%(ssn)s was created successfully"