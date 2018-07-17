import json

import requests
from django.http import HttpResponse


def CalcDelv(request):
    try:
        frm = request.GET.get('from')
        to = request.GET.get('to')
        response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + frm +"&destinations="+ to +"&language=ru-RU&sensor=false")
        dist = json.loads(response.content)['rows'][0]['elements'][0]['distance']['text'][:-3]
        return HttpResponse(dist)
    except:
        return HttpResponse(-1)



