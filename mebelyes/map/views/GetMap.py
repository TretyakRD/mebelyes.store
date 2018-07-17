from django.shortcuts import render


def GetMap(request):
    return render(request, 'map/GetMap.html')