from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Sample

def index(request):
    pass

def detail(request):
    pass

class IndexView(generic.ListView):
    template_name = 'sample/index.html'
    context_object_name = 'latest_sample_list'

    def get_queryset(self):
        """Return the last ten published samples."""
        return Sample.objects.order_by('-created')[:10]

class DetailView(generic.DetailView):
    model = Sample
    template_name = 'sample/detail.html'

