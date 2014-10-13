import collections

def build_ordered_dict():
    """Builds default ordered dict for use in poker.py and tests."""
    card_count = collections.OrderedDict()
    for face in ['A', 'K', 'Q', 'J']:
        card_count[face] = []
    for num in range(10, 1, -1):
        card_count[str(num)] = []

    return card_count

def sort_hand(hand):
    """Given a hand (list of strings), will sort in order from highest to lowest cards and return as a list of strings."""
    #OrderedDict should be an easier way to accomplish the sorting.
    card_count = build_ordered_dict()

    #convert face cards to numbers, turn each string into a tuple of (number, suite), sort, then turn back into a sorted list of strings.
    #OrderedDict suites aren't sorted. Do I care?
    #Int vs. string (face cards vs. numbers).
    for card in hand:
        suite = card[-1]
        score = card[0:2] if len(card) == 3 else card[0]
        card_count[score].append(suite)

    return card_count

def find_highest_hand(hand):
    """Given a hand (list of strings), will return the name of the highest ranking hand and a list of strings of the cards that fulfill it."""
    card_count = sort_hand(hand)

    pass

if __name__ == '__main__':
    # print find_highest_hand(['AD', 'QD', 'KD', '10D', 'JD'])
    print sort_hand(['AD', 'QD', 'KD', '10D', 'JD'])