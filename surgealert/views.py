from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	austin = {'start_latitude':'30.267277','start_longitude':'-97.743945','end_latitude':'30.267277','end_longitude':'-97.743945'}
	
	cities = []
	cities.append(austin)
	info = ''
	names = ["Austin"]

	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token AlPj9s0jvjkoIjBEpCDD__TbixVbdMdIgZq3Axk4'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + (names[cities.index(i)]) + '    '
		info = info + (data['prices'][0]['display_name']) + '    '
		info = info + str((data['prices'][0]['surge_multiplier'])) + '    '	
	return HttpResponse(info)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

