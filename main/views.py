from django.shortcuts import render

from .data import cards, news_cards, management_cards, facts_cards, emergency_cards, history_cards, people_cards, \
    photo_cards


# Create your views here.

def home(request):
    return render(request, 'main/index.html', {'cards':cards})

def news(request):
    return render(request, 'main/news.html', {'news_cards':news_cards})

def management(request):
    return render(request, 'main/management.html', {'management_cards':management_cards})

def contacts(request):
    return render(request, 'main/contacts.html',{'emergency_cards':emergency_cards})

def facts(request):
    return render(request, 'main/facts.html',{
        'facts_cards': facts_cards})

def history(request):
    return render(request, 'main/history.html',{
        'history_cards': history_cards
    })

def history_people(request):
    return render(request, 'main/history_people.html',{'people_cards': people_cards})


def history_photos(request):
    return render(request, 'main/history_photos.html',{'photo_cards':photo_cards})