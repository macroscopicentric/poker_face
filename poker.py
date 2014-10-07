def sort_hand(hand):
    """Given a hand (list of strings), will sort in order from highest to lowest cards and return as a list of strings."""
    pass

def find_highest_hand(hand):
    """Given a hand (list of strings), will return the name of the highest ranking hand and a list of strings of the cards that fulfill it."""
    sorted_hand = sort_hand(hand)

    pass

if __name__ == '__main__':
    print find_highest_hand(['AD', 'QD', 'KD', '10D', 'JD'])