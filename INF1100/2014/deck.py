import numpy as np
def make_deck():
    ranks = ['A', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Klover', 'Ruter', 'Hjerter', 'Spar']
    deck = []
    for s in suits:
        for r in ranks:
            deck.append(s+'-'+r)
    np.random.shuffle(deck)
    return deck

deck = make_deck()
card=deck.pop(0)
print card
