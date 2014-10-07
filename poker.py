def sort_hand(hand):
    """Given a hand (list of strings), will sort in order from highest to lowest cards and return as a list of strings."""
    face_cards_score = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
    sorted_hand = []

    #convert face cards to numbers, turn each string into a tuple of (number, suite), sort, then turn back into a sorted list of strings.
    for card in hand:
        if card[0] in face_cards_score:
            new_card = (face_cards_score[card[0]], card[1])
        else:
            new_card = (card[0], card[1])
        sorted_hand.append(new_card)

    sorted_hand.sort()

    return sorted_hand

def find_highest_hand(hand):
    """Given a hand (list of strings), will return the name of the highest ranking hand and a list of strings of the cards that fulfill it."""
    sorted_hand = sort_hand(hand)

    pass

if __name__ == '__main__':
    # print find_highest_hand(['AD', 'QD', 'KD', '10D', 'JD'])
    print sort_hand(['AD', 'QD', 'KD', '10D', 'JD'])