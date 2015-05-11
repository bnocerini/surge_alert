from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	downtown = {'start_latitude':'25.771100','start_longitude':'-80.192316','end_latitude':'25.771100','end_longitude':'-80.192316'}
	southbeach = {'start_latitude':'25.774694','start_longitude':'-80.133050','end_latitude':'25.774694','end_longitude':'-80.133050'}
	airport = {'start_latitude':'25.795029','start_longitude':'-80.278527','end_latitude':'25.795029','end_longitude':'-80.278527'}
	
	cities = []
	cities.append(downtown)
	cities.append(southbeach)
	cities.append(airport)
	info = ''
	names = ["Downtown","South Beach","Airport"]

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

