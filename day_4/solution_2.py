with open('puzzle.txt') as puzzle:
    cards_all = puzzle.readlines()
    cards = [0]*(len(cards_all)+1)

    for card in cards_all:
        card_deck = card.split(':')[1]
        card_number = int(card.split(':')[0].replace('Card ', ''))
        cards[card_number] += 1
        
        winning_card_deck = card_deck.split('|')[0]
        my_card_deck = card_deck.split('|')[1]
        set_winning_card_deck = set(winning_card_deck.split())
        set_my_card_deck = set(my_card_deck.split())
        total_matches = len(set_winning_card_deck.intersection(set_my_card_deck))
        
        for original_card in range(cards[card_number]):
            for copy_card in range(card_number+1, card_number+total_matches+1):
                cards[copy_card] += 1
   
        