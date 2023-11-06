# Name - Louis Cheng
# Date - 2023-09-16
# Description - Prebuilt python file of a Card and Deck class used to practice adding docstrings to for Assignment 3.

import random

class Card:
    """
    The Card class represents a single playing card and is initialised by passing a suit and number.
    """
    def __init__(self, suit, number):
        """
        Initializes a new Card instance with the specified suit and number.

        Args:
            suit (str): The suit of the card.
            number (str): The number or face of the card.
        """
        self._suit = suit
        self._number = number

    def __repr__(self):
        """
        Returns a string representation of the card.

        Returns:
            str: A string representing the card in the format "Number of Suit".
        """
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """
        Gets or sets the suit of the Card.

        Returns:
            str: The suit of the card.
        """
        return self._suit

    @suit.setter
    def suit(self, suit):
        # Setters don't need docstrings
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """
        Gets the number or face of the Card.

        Returns:
            str: The number or face of the card.
        """
        return self._number

    @number.setter
    def number(self, number):
        # Setters don't need docstrings
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:
    """
    The Deck class represents a deck of playing cards in order.
    """
    def __init__(self):
        """
        Initializes a new Deck instance and populates it with cards in order.
        """
        self._cards = []
        self.populate()

    def populate(self):
        """
        Populates the deck with cards in order.
        """
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        """
        Shuffles the deck randomly.
        """
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """
        Deals a specified number of cards from the deck.

        Args:
            no_of_cards (int): The number of cards to deal.

        Returns:
            list: A list of dealt cards.
        """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        """
        Returns a string representation of the deck.

        Returns:
            str: A string describing the number of cards in the deck.
        """
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
        
# Creating a deck and printing its representation
deck = Deck()
print(deck)