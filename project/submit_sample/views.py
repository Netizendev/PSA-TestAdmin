from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the page you will use to submit PSA test samples")