from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	alpharetta = {'start_latitude':'34.023493','start_longitude':'-84.234206','end_latitude':'34.023493','end_longitude':'-84.234206'}
	buckhead = {'start_latitude':'33.840954','start_longitude':'-84.379155','end_latitude':'33.840954','end_longitude':'-84.379155'}
	midtown = {'start_latitude':'33.783086','start_longitude':'-84.382319','end_latitude':'33.783086','end_longitude':'-84.382319'}
	
	cities = []
	cities.append(alpharetta)
	cities.append(buckhead)
	cities.append(midtown)
	info = ''
	names = ["Alpharetta","Buckhead","Midtown"]

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

