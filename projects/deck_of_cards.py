from random import shuffle


class Card:

    '''
    Each instance of Card should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
    Each instance of Card should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
    Card's __repr__ method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
    '''

    def __init__(self, suit, value):
        # Each instance of Card should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
        # Each instance of Card should have a value ("A", "2", "3", "4", "5",
        # "6", "7", "8", "9", "10", "J", "Q", "K").
        self.suit = suit
        self.value = value

    def __repr__(self):
        # Card's __repr__ method should return the card's value and suit (e.g.
        # "A of Clubs", "J of Diamonds", etc.)
        return "{} of {}".format(self.value, self.suit)
        # return f"{self.value} of {self.suit}"


# card_example = Card(suit="Hearts", value="A")
# print(card_example)

class Deck:

    '''
    Each instance of Deck should have a cards attribute with all 52 possible instances of Card
    Deck should have an instance method called count which returns a count of how many cards remain in the deck.
    Deck __repr__ method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
    Deck should have an instance method called _deal which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should raise a ValueError with the message "All cards have been dealt".
    Deck should have an instance method called shuffle which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise ValueError with the message "Only full decks can be shuffled" shuffle should return the shuffled deck.
    Deck should have an instance method called deal_card which uses the _deal method to deal a single card from the deck and return that single card.
    Deck should have an instance method called deal_hand which accepts a number and uses the _deal method to deal a list of cards from the deck and return that list of cards.
    '''

    def __init__(self):

        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = (
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K")

        '''
        Each instance of Deck should have a cards attribute with all 52 possible instances of Card
        Card("Hearts", "A")
        '''

        # option 1:
        self.cards = [Card(suit, value) for value in values for suit in suits]
        # print(len(self.cards))

        # option 2:
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(suit, value))

    def __repr__(self):
        # return f"Deck of {self.count()} cards"
        return "Deck of {} cards".format(self.count())

    def count(self):
        return len(self.cards)

    def _deal(self, deal_num):
        # check number of cards in deck
        deck_count = self.count()
        if deck_count == 0:
            raise ValueError("All cards have been dealt")

        # compare deck_count vs deal_num and return lower
        remove_num = min([deck_count, deal_num])
        # slice out removed_num cards from deck for hand and remaining_deck
        # starting from end/top
        hand = self.cards[-remove_num:]
        self.cards = self.cards[:-remove_num]

        return hand

    def deal_card(self):
        # returns only 1 card, not a list
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        # returns a list of cards
        return self._deal(hand_size)

    def shuffle_deck(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)

        # good practice to return self even though not necessary
        return self


deck = Deck()
