from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Here is our feedback-app :)")