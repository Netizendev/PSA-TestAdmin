from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Provsvar

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

class DetailView(generic.DetailView):
    model = Provsvar
    template_name = 'psa/detail.html'