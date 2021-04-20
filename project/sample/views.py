from django.http import HttpResponse
from .models import Sample

def index(request):
    latest_sample_list = Sample.objects.order_by('-created')[:5]
    output = ', '.join([q.ssn for q in latest_sample_list])
    return HttpResponse(output)