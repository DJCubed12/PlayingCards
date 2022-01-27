"""Hand class with algorithms to determine value."""

from .Card import Card, sort_cards
from . import PokerHands
from .Suits import all_suits


class Hand:
    """Contains cards that build with each other to form hands."""

    def __init__(self, cards: list):
        """Add the collection cards to the hand."""
        self.cards = cards

    def add(self, card: Card):
        """Add card to hand."""
        self.cards.append(card)

    def card_strs(self) -> list:
        """Get the hand's string as a list of card strings."""
        strs = []
        for card in self.cards:
            strs.append(str(card))
        return strs

    def copy(self):
        """Shallow copy of the hand. Creates a new Hand using the same Card objects."""
        new_cards = []
        for c in self.cards:
            new_cards.append(c)
        return Hand(new_cards)


    def make_histograms(self):
        """Create value and suit histograms. The histograms have a key of int and Suit, respectively, and a value of a list of cards."""
        # Empty lists for all suits to start with
        self.suit_spread = {suit: [] for suit in all_suits}
        for card in self.cards:
            # Add card to suit's list
            self.suit_spread[card.suit].append(card)
        for suit, cards in self.suit_spread.items():
            self.suit_spread[suit] = sort_cards(cards)

        self.value_spread = dict()
        for card in self.cards:
            try:
                # Add card to list if possible
                self.value_spread[card.value].append(card)
            except KeyError:
                # If not possible, create list containing card
                self.value_spread[card.value] = [card]


    def evaluate_poker(self):
        """Creates the best poker hand possible with the cards and returns it. Returns PokerHands.PokerHand or one of its children."""
        self.make_histograms()

        flush = self.flush_check()
        straight = self.straight_check()
        kinds = self.of_a_kind_check()

        # Worst -> Best
        # (PokerHand, Pair, Two_Pair, Three_Kind, Straight, Flush, Full_House, Four_Kind, Straight_Flush, Royal_Flush)

        if straight:
            if flush:
                # Possible Straight Flush
                straight_flush = []
                for n in straight:
                    for card in n:
                        if card in flush:
                            straight_flush.append(card)
                            break
                    else:
                        straight_flush = []
                
                if len(straight_flush) >= 5:
                    # Straight Flush Found, Possible Royal Flush
                    if straight_flush[0].value == 14:
                        # Royal Flush
                        return PokerHands.Royal_Flush(straight_flush)

                    # Straight Flush (not Royal Flush)
                    return PokerHands.Straight_Flush(straight_flush)
                    
            
            # Straight (regular)
            straight_only_5 = []
            i = 0
            while len(straight_only_5) < 5:
                # Get the first card listed under each number until straight is 5 long
                straight_only_5.append(straight[i][0])
                i += 1
            # Don't return it, A 4 of a kind, Full House, or Flush can still be better
            straight = PokerHands.Straight(straight_only_5)

        if kinds[4]:
            # Four of a kind
            four_kind = kinds[4][0]
            return PokerHands.Four_Kind(self.fill_pokerhand(four_kind))
        
        if kinds[3]:
            # Possible Full House
            three_kind = kinds[3][0]
            if kinds[2]:
                # Full House
                for card in kinds[2][0]:
                    three_kind.append(card)
                return PokerHands.Full_House(three_kind)

        # Now that we know there's no Full House, check again for straights and flushes
        if flush:
            return PokerHands.Flush(flush[:5])
        if straight:
            # Straight should already be made.
            return straight

        if kinds[3]:
            # Three of a kind (Not Full House; already checked)
            three_kind = kinds[3][0]
            return PokerHands.Three_Kind(self.fill_pokerhand(three_kind))

        if kinds[2]:
            # Pair; Possible Two Pair
            pair = kinds[2][0]

            if len(kinds[2]) >= 2:
                # Two Pair
                for card in kinds[2][1]:
                    pair.append(card)
                return PokerHands.Two_Pair(self.fill_pokerhand(pair))

            # Pair (regular)
            return PokerHands.Pair(self.fill_pokerhand(pair))
        
        # High Card
        return PokerHands.PokerHand(self.fill_pokerhand([]))

    def fill_pokerhand(self, hand: list):
        """Attempts to fill a pokerhand with the highest cards not already present. Returns the filled list."""
        for value in range(14, 1, -1):
            try:
                card = self.value_spread[value][0]
                if not (card in hand):
                    hand.append(card)
            except KeyError:
                pass

            if len(hand) >= 5:
                return hand

        # Unable to fill hand
        return hand

    def flush_check(self):
        """Check for a flush. Returns list of ALL cards in flush or False if there isn't one."""
        for _, cards in self.suit_spread.items():
            if len(cards) >= 5:
                return cards
        return False

    def straight_check(self):
        """Check for a straight. Returns a list if found, False otherwise. Highest straight preferred.
        
        Returns
        -------
        list(list(Card))
            Returned if a straight is found. The inner list are cards of the same value. Those inner lists are ordered highest value first in the outer list.
        False
            Returned when straight is not found.
        """
        straight = []
        # Iterates through each possible card value
        for value in range(14, 1, -1):
            try:
                cards = self.value_spread[value]
                straight.append(cards)
            except KeyError:
                # value was not found, therefore the straight has ended.
                if len(straight) >= 5:
                    # A straight was found.
                    return straight
                straight = []
        
        return False

    def of_a_kind_check(self):
        """Detects if their are cards with the same value. Returns a dictionary of pairs, three-of-a-kinds, and four-of-a-kinds. Each sorted highest first.
        
        Returns
        -------
        dict(int: list(Card))
            2, 3, and 4 are keys representing how many cards have the same value. Each dictionary value is a list of Card lists with the same value.
        """
        of_a_kinds = {
            2: [],
            3: [],
            4: []
        }
        for _, cards in self.value_spread.items():
            try:
                of_a_kinds[len(cards)].append(cards)
            except KeyError:
                pass

        return of_a_kinds


    def __len__(self):
        return len(self.cards)

    def __str__(self):
        strs = ""
        for card in self.cards:
            strs += str(card) + ', '
        return strs[:-2]