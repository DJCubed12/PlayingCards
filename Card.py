"""Player Card class."""

from .Suits import all_suits


def sort_cards(cards: list):
    """Sort a list of cards by value."""
    return sorted(cards, reverse=True, key=lambda c: c.value)

def get_card_dict():
    """Returns a dictionary of all possible cards. Keys are strings with the capitalized first letter of the suit followed by the value (2-10, Jack, Queen, King, Ace)."""
    end = dict()
    for suit in all_suits:
        key = suit.name[0]
        for value in range(14, 1, -1):
            card = Card(value, suit)
            end[key + card.value_str()] = card
    return end
    

class Card:
    """A singular playing card. Comparison operations are used for high card testing.
    
    Instance Variables
    ------------------
    suit : Suit
        A Suit object from .Suits.Suit.
    value : int
        Integer value of the card. Jack = 11, Queen = 12, King = 13, Ace = 14.
    """

    def __init__(self, value: int, suit):
        if value == 1:
            value = 14
        self.value = value
        self.suit = suit

    def value_str(self):
        """The value of the card as a string."""
        if self.value > 10:
            if self.value == 14:
                return "Ace"
            elif self.value == 13:
                return "King"
            elif self.value == 12:
                return "Queen"
            elif self.value == 11:
                return "Jack"
        return str(self.value)

    def __str__(self):
        return self.value_str() + ' of ' + str(self.suit)


    def __lt__(self, other):
        if isinstance(other, Card):
            if self.value < other.value:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.value < other:
                return True
            else:
                return False

        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Card):
            if self.value <= other.value:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.value <= other:
                return True
            else:
                return False

        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Card):
            if self.value > other.value:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.value > other:
                return True
            else:
                return False

        return NotImplemented
        
    def __ge__(self, other):
        if isinstance(other, Card):
            if self.value >= other.value:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.value >= other:
                return True
            else:
                return False

        return NotImplemented
        
    def __eq__(self, other):
        """Test value equality, ignores suit."""
        if isinstance(other, Card):
            if self.value == other.value:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.value == other:
                return True
            else:
                return False

        return NotImplemented

    def __ne__(self, other):
        """Test value equality, ignores suit."""
        try:
            return not(self == other)
        except:
            return NotImplemented

    def __and__(self, other):
        """Test whether the cards are the same (same value and suit)."""
        if isinstance(other, Card):
            return (self.value == other.value) and (self.suit is other.suit)
        return NotImplemented

    def __or__(self, other):
        """Test whether the cards are the same suit."""
        if isinstance(other, Card):
            return self.suit is other.suit
        return NotImplemented
