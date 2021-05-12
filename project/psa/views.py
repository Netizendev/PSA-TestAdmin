from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy

from .models import Provsvar, Patient, Kallelse


def index(request):
	provsvar = Provsvar.objects.all()

	form = ProvsvarForm()

	if request.method == 'POST':
		item.delete()
		return redirect('/')
	

	context = {'provsvar':provsvar, 'form':form}
	return render(request, 'psa/index.html', context)



def detail(request):
    pass


class IndexView(generic.ListView):
    template_name = 'psa/index.html'
    context_object_name = 'latest_provsvar_list'

    def get_queryset(self):
        """Visar de tio senaste provsvaren."""
        return Provsvar.objects.order_by('-created')[:10]
        
class DetailView(generic.DetailView):
    model = Provsvar
    template_name = 'psa/detail.html'

class DetailView2(generic.DetailView):
    model = Hantera
    template_name = 'psa/detail.html'

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

class IndexView2(generic.ListView):
    template_name = 'psa/index.html'
    context_object_name = 'latest_hantera_list'

    def get_queryset(self):
        """Visar de tio senaste provsvaren."""
        return Hantera.objects.order_by('result')[:100]