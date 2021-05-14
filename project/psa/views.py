from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy

from .models import Provsvar, Patient, Hantera

# def index(request):
#     pass

# def detail(request):
#     pass


class IndexView(generic.ListView):
    template_name = 'psa/index.html'
    context_object_name = 'latest_provsvar_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'latest_provsvar_list': Provsvar.objects.order_by('-created')[:10],
            'patient_list': Patient.objects.order_by('-created'),
        })
        return context

    def get_queryset(self):
        return Patient.objects.all()

class ProvsvarDetail(generic.DetailView):
    model = Provsvar
    template_name = 'psa/detail.html'

class PatientDetail(generic.DetailView):
    model = Patient
    template_name = 'psa/patient.html'

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