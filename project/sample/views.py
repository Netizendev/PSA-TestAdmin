from django.shortcuts import render, get_object_or_404

from .models import Sample


def index(request):
    latest_sample_list = Sample.objects.order_by('-created')[:5]
    context = {'latest_sample_list': latest_sample_list}
    return render(request, 'sample/index.html', context)

def detail(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    return render(request, 'sample/detail.html', {'sample': sample})