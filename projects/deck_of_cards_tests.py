import unittest
from deck_of_cards import Card
from deck_of_cards import Deck

class CardTests(unittest.TestCase):
    
    def setUp(self):
        self.card = Card("Hearts", "A")
    
    def test_init(self):
        pass
    
    def test_repr(self):
        pass

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    

# python3 deck_of_cards_tests.py -v

if __name__ == "__main__":
    unittest.main()