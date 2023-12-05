points = 0
with open('puzzle.txt') as puzzle:
    for card in puzzle.readlines():
        card_deck = card.split(':')[1]
        winning_card_deck = card_deck.split('|')[0]
        my_card_deck = card_deck.split('|')[1]
        set_winning_card_deck = set(winning_card_deck.split())
        set_my_card_deck = set(my_card_deck.split())
        
        if len(set_winning_card_deck.intersection(set_my_card_deck)) == 0:
            points+=0
        else:
            points+=2**(len(set_winning_card_deck.intersection(set_my_card_deck))-1)
