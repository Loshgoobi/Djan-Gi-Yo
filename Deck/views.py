from django.shortcuts import render
import logging
from Deck.models import Cards
from .models import Player

def deck(request):
    logger = logging.getLogger(__name__)
    logger.info('test log deck')
    Cardes = Cards.objects.all()
    # TODO : get player from session and put his hand in a var
    #resultSet2 = Player.objects.first().hand
    return render(request, 'deck.html', locals())