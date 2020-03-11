from django.shortcuts import render, redirect, get_object_or_404
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
            url = Url(original_url=original_url)
            error = 'Please submit a valid url!'
            return render(request, 'urls/index.html', {'error': error, 'url': url})
    

def url_redirect(request, shortened_url):
    url = get_object_or_404(Url, shortened_url=shortened_url)
    original_url = url.original_url

    if (original_url[:4].lower() != 'http'):
        original_url = 'http://' + original_url
	
    return redirect(original_url)