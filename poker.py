def sort_hand(hand):
    """Given a hand (list of strings), will sort in order from highest to lowest cards and return as a list of strings."""
    face_cards_score = {'A': 14, 'K': 13, 'Q': 12, 'J': 11}
    reverse_face_cards = {14: 'A', 13: 'K', 12: 'Q', 11: 'J'}
    sorted_hand = []

    #convert face cards to numbers, turn each string into a tuple of (number, suite), sort, then turn back into a sorted list of strings.
    #this doesn't currently address sorting the suites.
    for card in hand:
        if card[0] in face_cards_score:
            #if it's a face card
            new_card = (face_cards_score[card[0]], card[1])
        elif len(card) == 3:
            #if the card is a 10, it's a different string length
            new_card = (int(card[0:2]), card[2])
        else:
            new_card = (int(card[0]), card[1])
        sorted_hand.append(new_card)

    sorted_hand.sort()
    #sorting from highest to lowest in the assumption that the best scoring hand will include the highest cards possible.
    sorted_hand.reverse()

    sorted_hand = [str(reverse_face_cards[card[0]]) + card[1] if card[0] in reverse_face_cards else str(card[0]) + card[1] for card in sorted_hand]

    return sorted_hand

def find_highest_hand(hand):
    """Given a hand (list of strings), will return the name of the highest ranking hand and a list of strings of the cards that fulfill it."""
    sorted_hand = sort_hand(hand)

    pass

if __name__ == '__main__':
    # print find_highest_hand(['AD', 'QD', 'KD', '10D', 'JD'])
    print sort_hand(['AD', 'QD', 'KD', '10D', 'JD'])