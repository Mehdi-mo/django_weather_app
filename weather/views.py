# this is my views.py
from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=45EB9E13-ED62-47F8-8C8E-623A1963EE63")


    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error..."


    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=45EB9E13-ED62-47F8-8C8E-623A1963EE63
    return render(request, 'weather/home.html', {'api': api})


def aboutus_view(request):
    return render(request, 'aboutus.html')