from django.shortcuts import render
from . import urls

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=BA923036-43A0-4D94-B406-EBDBA7F86210")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = 'Error'


	return render(request, 'home.html', {'api': api})

def about(request):

	return render(request, 'about.html', {})

def contact(request):

	return render(request, 'contact.html', {})