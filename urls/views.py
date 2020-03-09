from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Url

def index(request):
    if request.method == 'GET':
        return render(request, 'urls/index.html', {'url': None})

    elif request.method == 'POST':
        original_url = request.POST['original_url']
        
        try:
            url = Url.objects.get(original_url=original_url)
        except Url.DoesNotExist:
            url = None

        if (url):
            return render(request, 'urls/index.html', {'url': url})
        else:
            pass
    
