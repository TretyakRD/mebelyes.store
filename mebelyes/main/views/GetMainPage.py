from django.shortcuts import render

from api.models import Post


def GetMainPage(request):
    post = Post.objects.filter(id=2)
    data = {}
    for el in post:
        data = el

    return render(request, 'main/GetMainPage.html', {'disc': data.content})