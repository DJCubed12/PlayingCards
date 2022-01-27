"""Houses the PokerHand base class (high card hand) and its subclasses (every other hand type in poker). Also, hand_hierarchy, which defines what hands are best."""

from .Card import Card, sort_cards


class PokerHand:
    """Up to 5 cards of no relavence to eachother."""

    def __init__(self, cards: list):
        """Be sure that cards are already properly sorted."""
        self.cards = cards
        self.tested_high = False

    def __str__(self):
        return f"{self.cards[0].value_str()} High"

    def card_strs(self) -> list:
        """Get the hand's string as a list of card strings."""
        strs = []
        for card in self.cards:
            strs.append(str(card))
        return strs

    def full_str(self) -> str:
        """Get the hand's string as a common separated string of card strings."""
        end = ''
        for s in self.card_strs():
            end += s + ', '
        return end[:-2]


    def __len__(self):
        return len(self.cards)

    def __and__(self, other):
        """Detects if they are the same hand type."""
        if isinstance(other, PokerHand):
            if self.__class__ is other.__class__:
                return True
            return False
        return NotImplemented


    def __lt__(self, other):
        if isinstance(other, PokerHand):
            # Is a poker hand
            if self.__class__ is other.__class__:
                # Same type of poker hand
                for i in range(5):
                    try:
                        this_card = self.cards[i]
                        other_card = other.cards[i]
                    except IndexError:
                        if len(self.cards) < len(other.cards):
                            return True
                        elif len(self.cards) > len(other.cards):
                            raise False
                        else:
                            raise self.EqualHands(self, other)

                    if this_card < other_card:
                        return True
                    elif this_card > other_card:
                        return False
                    # They are equal, go to next
                    self.tested_high = True

                # All cards were equal
                raise self.EqualHands(self, other)
            else:
                # Either lower or higher in hierarchy
                rank_self = hand_hierarchy.index(self.__class__)
                rank_other = hand_hierarchy.index(other.__class__)
                if rank_self < rank_other:
                    return True
                else:
                    return False
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, PokerHand):
            # Is a poker hand
            if self.__class__ is other.__class__:
                # Same type of poker hand
                for i in range(5):
                    try:
                        this_card = self.cards[i]
                        other_card = other.cards[i]
                    except IndexError:
                        if len(self.cards) > len(other.cards):
                            return True
                        elif len(self.cards) < len(other.cards):
                            raise False
                        else:
                            raise self.EqualHands(self, other)

                    if this_card > other_card:
                        return True
                    elif this_card < other_card:
                        return False
                    # They are equal, go to next
                    self.tested_high = True
                
                # All cards were equal
                raise self.EqualHands(self, other)
            else:
                # Either lower or higher in hierarchy
                rank_self = hand_hierarchy.index(self.__class__)
                rank_other = hand_hierarchy.index(other.__class__)
                if rank_self > rank_other:
                    return True
                else:
                    return False
        return NotImplemented

    class EqualHands(Exception):
        """Raised if two hands were found to be equal during comparison."""
        pass

    def __eq__(self, other):
        if isinstance(other, PokerHand):
            if self.__class__ is other.__class__:
                try:
                    # If this doesn't raise EqualHands, drop out of if and return False.
                    self < other
                except self.EqualHands:
                    self.tested_high = False
                    return True
            return False
        return NotImplemented

    def __ne__(self, other):
        result = self == other
        if result is NotImplemented:
            return result
        return not result


class Pair(PokerHand):
    """Two cards of the same value."""

    def __str__(self):
        return f"Pair of {self.cards[0].value_str()}s"

class Two_Pair(PokerHand):
    """Two separate pairs."""

    def __str__(self):
        return f"Two Pair of {self.cards[0].value_str()}s and {self.cards[2].value_str()}s"

class Three_Kind(PokerHand):
    """Three cards of the same value."""

    def __str__(self):
        return f"Three-of-a-kind {self.cards[0].value_str()}s"

class Straight(PokerHand):
    """5 consecutive cards."""

    def __str__(self):
        return f"{self.cards[0].value_str()} high Straight"

class Flush(PokerHand):
    """5 cards all of the same suit."""
    
    def __str__(self):
        return f"{self.cards[0].value_str()} high Flush"

class Full_House(PokerHand):
    """A Three-of-a-kind and pair."""

    def __str__(self):
        return f"Full House of {self.cards[0].value_str()}s and {self.cards[-1].value_str()}s"

class Four_Kind(PokerHand):
    """Four cards of the same value."""

    def __str__(self):
        return f"Four-of-a-kind {self.cards[0].value_str()}s"

class Straight_Flush(PokerHand):
    """5 consecutive cards of the same suit."""

    def __str__(self):
        return f"{self.cards[0].value_str()} high Straight Flush"

class Royal_Flush(PokerHand):
    """Ace, King, Queen, Jack, 10 all of the same suit."""

    def __str__(self):
        return "Royal Flush"


hand_hierarchy = (PokerHand, Pair, Two_Pair, Three_Kind, Straight, Flush, Full_House, Four_Kind, Straight_Flush, Royal_Flush)