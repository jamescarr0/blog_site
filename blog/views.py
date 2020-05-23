from django.shortcuts import render


def index(request):
    """ The home page for users blog articles. """
    return render(request, 'index.html')
