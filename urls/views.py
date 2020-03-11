from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Url
from hashids import Hashids

def index(request):
    if request.method == 'GET':
        return render(request, 'urls/index.html')

    elif request.method == 'POST':
        original_url = request.POST['original_url']

        # Check is an url
        if ('.' in original_url):        
            try:
                check = Url.objects.get(original_url=original_url)
            except Url.DoesNotExist:
                check = False

            if (check):
                return render(request, 'urls/index.html', {'url': check})
            else:
                url = Url(original_url=original_url)
                url.save()

                hashids = Hashids(min_length=4)
                shortened_url = hashids.encode(url.id)
                url.shortened_url = shortened_url
                url.save()

                return render(request, 'urls/index.html', {'url': url})
        else:
            error = 'Please submit a valid url!'
            return render(request, 'urls/index.html', {'error': error})
    
