from django.shortcuts import render

from api.models.Post import Post


def Offer(request):

    post = Post.objects.filter(id=1)
    data = {}
    for el in post:
        data = el

    context={
        'title':data.title,
        'content':data.content
    }
    return render(request, 'main/Offer.html', context)