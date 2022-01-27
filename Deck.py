"""Deck of cards."""

from random import shuffle

from Card import Card
from Suits import all_suits

class Deck:
        """A standard 52 card deck. No jokers.
        
        Instance Variables
        ------------------
        _deck : list(Card)
            The actual set of cards contained. _deck[-1] is considered the top of the deck.
        size (property) : int
            Number of cards in deck.
        """

        def __init__(self, shuffle=True):
            """Create a normal 52 card deck a shuffle it."""
            self._deck = []
            for suit in all_suits:
                for value in range(2, 15):
                    self._deck.append(Card(value, suit))
            if shuffle:
                self.shuffle()
        
        @property
        def size(self):
            """Get the current size of the deck."""
            return len(self._deck)


        def add(self, card: Card):
            """Add card to the top of the deck."""
            self._deck.append(card)

        def bury(self, card: Card):
            """Add card to the bottom of the deck."""
            self._deck.insert(0, card)

        def draw(self, n=1):
            """Draw the top n cards. Returns Card with default n=1, or list(Card) if n>1."""
            draws = []
            for x in range(n):
                draws.append(self._deck.pop())
            
            if len(draws) == 1:
                return draws[0]
            return draws

        def contains(self, card: Card):
            """Returns True if Card is in deck, False otherwise."""
            for c in self._deck:
                if c & card:
                    return True
            return False
        
        def remove(self, card: Card):
            """Remove the first card that matches (suit & value). Returns True if card was found, False otherwise."""
            for i, c in enumerate(self._deck):
                if c & card:
                    self._deck.pop(i)
                    return True
            return False

        def shuffle(self):
            shuffle(self._deck)


        def __str__(self):
            return f"{self.size} card deck"

        def __len__(self):
            return self.size