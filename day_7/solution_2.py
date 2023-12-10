
strength_sorted_cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3' , '2', 'J']
types = ['5K', '4K', 'FH', '3K', '2P', '1P', 'HC']

def get_strength(hand: str):
    return [len(strength_sorted_cards)-strength_sorted_cards.index(card) for card in hand]

def get_card_strength(card: str):
    return len(strength_sorted_cards)-strength_sorted_cards.index(card)

def assign_hand_type(hand: list):
    hand_wo_joker = [card for card in hand if card != 'J']
    card_count = [hand_wo_joker.count(card) for card in set(hand_wo_joker)]

    number_of_jokers = hand.count('J')
    if len(set(hand_wo_joker)) == 1:
        hand_type = '5K'
    elif len(set(hand_wo_joker)) == 2:
        if number_of_jokers >1:
            hand_type = '4K'
        elif number_of_jokers == 1:
            if max(card_count) == 3:
                hand_type = '4K'
            else:
                hand_type = 'FH'
        elif number_of_jokers == 0:
            if (hand.count(hand[0]) == 4) | (hand.count(hand[0]) == 1):
                hand_type = '4K'
            else:
                hand_type = 'FH'
        
    elif len(set(hand_wo_joker)) == 3:
        if number_of_jokers==0:        
            if 3 in card_count:
                hand_type = '3K'
            else:
                hand_type = '2P'
        else:
            hand_type = '3K'

    elif len(set(hand_wo_joker)) == 4:
        hand_type = '1P'
    elif len(set(hand_wo_joker)) == 0:
        hand_type = '5K'
    else:
        hand_type = 'HC'
    return hand_type

def assign_hand_type_strength(hand_type: str, cards):
    if hand_type == '5K':
        return get_strength(hand)[0]
    elif hand_type == '4K':
        quadruple_card = [card for card in set(hand) if hand.count(card) == 4][0]
        return get_strength(quadruple_card)[0]
    elif hand_type == 'FH':
        triple_card = [card for card in set(hand) if hand.count(card) == 3][0]
        return get_strength(triple_card)[0]
    elif hand_type == '3K':
        triple_card = [card for card in set(hand) if hand.count(card) == 3][0]
        return get_strength(triple_card)[0]
    elif hand_type == '2P':
        pair_cards = [card for card in set(hand) if hand.count(card) == 2]
        return max(get_strength(pair_cards))
    elif hand_type == '1P':
        pair_card = [card for card in set(hand) if hand.count(card) == 2][0]
        return get_strength(pair_card)[0]
    else:
        return max(get_strength(hand))
    

with open('puzzle.txt') as f:
    data = f.read().split('\n')
    
data = [line.split() for line in data]
cards = [card[0] for card in data]
bets = [bet[1] for bet in data]

hand_types = {}
hand_strengths = {}
hand_bets = {}
for hand in cards:
    hand_types[hand] = assign_hand_type(hand)
    hand_strengths[hand] = [get_card_strength(hand[position]) for position in range(5)]
    hand_bets[hand] = bets[cards.index(hand)]

# group keys in hand_types with same values into a list, i.e. getting {v1: [k1, k2, ...], v2: [k3, k4, ...], ...}
grouped = {v: [k for k in hand_types.keys() if hand_types[k] == v] for v in hand_types.values()}

# sort each list in grouped by hand_strengths
sorted_grouped = {k: sorted(v, key=lambda x: hand_strengths[x], reverse=True) for k, v in grouped.items()}

hands_sorted_by_strength = []
for type in types:
    if type in sorted_grouped.keys():
        hands_sorted_by_strength.extend(sorted_grouped[type])

# calculate bets
bets_aggregated=0
for i, hand in enumerate(hands_sorted_by_strength):
    bets_aggregated += int(hand_bets[hand])*(len(hands_sorted_by_strength)-i)

print(bets_aggregated)