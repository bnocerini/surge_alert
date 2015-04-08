from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Greeting

# Create your views here.
def index(request):
	athens = {'start_latitude':'33.957423','start_longitude':'-83.376847','end_latitude':'33.957423','end_longitude':'-83.376847'}
	sanantoniopearl = {'start_latitude':'29.442322','start_longitude':'-98.479279','end_latitude':'29.442322','end_longitude':'-98.479279' }
	atlantabuckhead = {'start_latitude':'33.840954','start_longitude':'-84.379155','end_latitude':'33.840954','end_longitude':'-84.379155'}
	koreatown = {'start_latitude':'34.069112','start_longitude':'-118.281384','end_latitude':'34.019479','end_longitude':'-118.401718'}
	midwilshire = {'start_latitude':'34.057166','start_longitude':'-118.323956','end_latitude':'34.019479','end_longitude':'-118.401718'}
	downtown = {'start_latitude':'34.042943','start_longitude':'-118.260098','end_latitude':'34.019479','end_longitude':'-118.401718'}
	glendale = {'start_latitude':'34.137907','start_longitude':'-118.250141','end_latitude':'34.019479','end_longitude':'-118.401718'}
	northhollywood = {'start_latitude':'34.161161','start_longitude':'-118.358803','end_latitude':'34.019479','end_longitude':'-118.401718'}

	cities = []
	cities.append(athens)
	cities.append(sanantoniopearl)
	cities.append(atlantabuckhead)
	cities.append(koreatown)
	cities.append(midwilshire)
	cities.append(downtown)
	cities.append(glendale)
	cities.append(northhollywood)
	info = ''
	names = ["Athens","San Antonio Pearl","Atlanta Buckhead","Koreatown","Midwilshire","Downtown","Glendale","North Hollywood"]

	for i in cities:
		payload = cities[cities.index(i)]
		headers = {'Authorization':'Token AlPj9s0jvjkoIjBEpCDD__TbixVbdMdIgZq3Axk4'}
		r = requests.get('https://api.uber.com/v1/estimates/price', params = payload, headers=headers)
		data = json.loads(r.text)
		info = info + (names[cities.index(i)]) + '    '
		info = info + (data['prices'][0]['display_name']) + '    '
		info = info + str((data['prices'][0]['surge_multiplier'])) + '  <br/><br/>'	
	return HttpResponse(info)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

