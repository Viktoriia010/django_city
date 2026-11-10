from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/index.html')

def news(request):
    return render(request, 'main/news.html')

def management(request):
    return render(request, 'main/management.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def facts(request):
    return render(request, 'main/facts.html')

def history(request):
    return render(request, 'main/history.html')

def history_people(request):
    return render(request, 'main/history_people.html')


def history_photos(request):
    return render(request, 'main/history_photos.html')