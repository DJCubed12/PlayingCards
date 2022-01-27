from Card import Card, sort_cards
from Deck import Deck
from Suits import Diamonds, Hearts, Clubs, Spades


def test_sequence():
    card_sort()

    deck = Deck()
    deck_creation(deck)
    deck_draw(deck)


def card_sort():
    cards = [
        Card(5, Spades),
        Card(10, Hearts),
        Card(13, Diamonds),
        Card(10, Spades),
        Card(8, Hearts),
        Card(14, Spades),
        Card(2, Diamonds)
    ]

    cards = sort_cards(cards)
    last = cards.pop(0)
    for card in cards:
        assert last >= card, f"{last} was sorted higher than {card}."
        last = card

    print("Card Sorting Test Passed")

def deck_creation(deck=Deck()):
    assert (s := deck.size) == 52, f"Deck has only {s} cards."

    sample = [
        Card(14, Spades),
        Card(2, Clubs),
        Card(10, Diamonds),
        Card(7, Hearts)
    ]
    for card in sample:
        assert deck.contains(card), f"{card} not in deck."

    print("Creation Test Passed")

def deck_draw(deck=Deck()):
    before = deck.size
    card = deck.draw()
    assert isinstance(card, Card), "Drawing 1 card did not return a Card."
    after = deck.size
    assert (before - 1) == after, f"Deck lost {before-after} cards after drawing 1."
    assert not(deck.contains(card)), "Deck contained a card drawn."

    before = after
    cards = deck.draw(3)
    assert isinstance(cards, list), "Drawing 3 cards did not return a list."
    after = deck.size
    assert (before - 3) == after, f"Deck lost {before-after} cards after drawing 3."
    for card in cards:
        assert not deck.contains(card), "Deck contained a card drawn."

    print("Draw Tests Passed")


if __name__ == "__main__":
    test_sequence()