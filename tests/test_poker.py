import unittest
from nose.tools import eq_

from poker_face.poker import sort_hand, find_highest_hand

class TestSortHand(unittest.TestCase):
    pass

class TestFindHighestHand(unittest.TestCase):
    def test_royal_flush(self):
        result = find_highest_hand(['10S', 'JS', 'QS', 'KS', 'AS'])
        expected_result = ('Royal Flush', ['AS', 'KS', 'QS', 'JS', '10S'])
        eq_(result, expected_result)

    def test_straight_flush(self):
        result = find_highest_hand(['4H', '5H', '6H', '7H', '8H'])
        expected_result = ('Straight Flush', ['8H', '7H', '6H', '5H', '4H'])
        eq_(result, expected_result)

    def test_four_of_a_kind(self):
        result = find_highest_hand(['QS', 'QD', 'QC', 'QH', '5S'])
        expected_result = ('Four of a Kind', ['QS', 'QC', 'QD', 'QH'])
        eq_(result, expected_result)

    def test_full_house(self):
        result = find_highest_hand(['KS', 'KD', '3C', '3H', '3D'])
        expected_result = ('Full House', ['KS', 'KD', '3C', '3D', '3H'])
        eq_(result, expected_result)

    def test_flush(self):
        result = find_highest_hand(['AD', 'QD', '6D', 'JD', '2D'])
        expected_result = ('Flush', ['AD', 'QD', 'JD', '6D', '2D'])
        eq_(result, expected_result)

    def test_straight(self):
        result = find_highest_hand(['KS', 'QD', 'JS', '10H', '9S'])
        expected_result = ('Straight', ['KS', 'QD', 'JS', '10H', '9S'])
        eq_(result, expected_result)

    def test_three_of_a_kind(self):
        result = find_highest_hand(['5D', 'JC', '8H', '8C', '8D'])
        expected_result = ('Three of a Kind', ['8C', '8D', '8H'])
        eq_(result, expected_result)

    def test_two_pair(self):
        result = find_highest_hand(['10S', 'QD', '7S', 'QC', '7H'])
        expected_result = ('Two Pair', ['QC', 'QD', '7S', '7H'])
        eq_(result, expected_result)

    def test_pair(self):
        result = find_highest_hand(['10S', 'JD', '7S', '6H', '6S'])
        expected_result = ('Pair', ['6S', '6H'])
        eq_(result, expected_result)

    def test_high_card(self):
        result = find_highest_hand(['7S', '6H', '4S', '3D', '2C'])
        expected_result = ('High Card', ['7S'])
        eq_(result, expected_result)