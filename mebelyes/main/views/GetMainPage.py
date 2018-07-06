from django.shortcuts import render


def GetMainPage(request):
    return render(request, 'main/MainPage.html')