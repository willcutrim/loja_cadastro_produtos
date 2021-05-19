from django.shortcuts import render, HttpResponse

def index(request):
    h = 'Salve rapaziada da Twitch'
    return render(request, 'html/index.html', {'h':h})


