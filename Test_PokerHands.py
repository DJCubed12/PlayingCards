"""Test functions for Hands.Hand creation, Hands.Hand.evaulate_poker, PokerHands.PokerHand and children creation and comparison."""

from Card import Card, get_card_dict
from Deck import Deck
from Hand import Hand
from PokerHands import PokerHand
from Suits import Spades, Clubs, Hearts, Diamonds


def interactive_test():
    """Test poker hands in an interactive console environment."""
    print("\nPoker Hand Interactive Testing Environment")
    print("------------------------------------------\n")

    player_count = int(input("How many players: "))
    print("-------------------\n")

    while True:
        deck = Deck()
        table = Hand([])

        print(" - - - NEW GAME - - - ")
        print()

        # Pre-flop / Init
        players = []
        for i in range(player_count):
            players.append(Hand(deck.draw(2)))
        print("THE DEAL\n")
        turn(table, players)

        # Flop
        for i in range(3):
            card = deck.draw()
            table.add(card)
            for hand in players:
                hand.add(card)
        print("THE FLOP\n")
        turn(table, players)

        # Turn
        card = deck.draw()
        table.add(card)
        for hand in players:
            hand.add(card)
        print("THE TURN\n")
        turn(table, players)

        # River
        card = deck.draw()
        table.add(card)
        for hand in players:
            hand.add(card)
        print("THE RIVER\n")
        turn(table, players)
        
def turn(table: Hand, hands: list):
    """Display every hand (including table), evaluate each, display winner, and wait for input."""

    print("Table:")
    print(table)
    print()

    pokerhands = []
    for hand in hands:
        pokerhands.append(hand.evaluate_poker())
    
    winner = None
    draw = []
    for i, hand in enumerate(pokerhands):
        try:
            if winner is None:
                winner = i
            elif hand > pokerhands[winner]:
                winner = i
        except PokerHand.EqualHands:
            winner = i
            draw.append(winner)
    
    for i, hand in enumerate(hands):
        title_str = f"Player {i}: "
        if draw:
            if (i in draw) or (i == winner):
                title_str += "(Draw)"
        elif i == winner:
            title_str += "(Winner)"

        print(title_str)
        print(pokerhands[i])
        print(hand)
        print()

    wait_for_user()

def wait_for_user():
    inp = input("Enter q to quit or anything else to continue.\n")
    print("- - - - - - - - - - - - - - - - - - - - - - -\n")
    if 'q' in inp.lower():
        raise EndTest()


def test_cases():
    """Use specific test cases.
    (PokerHand, Pair, Two_Pair, Three_Kind, Straight, Flush, Full_House, Four_Kind, Straight_Flush, Royal_Flush)
    """
    c = get_card_dict()
    hands = [
        Hand([c['SAce'], c['SKing'], c['SQueen'], c['SJack'], c['S10']]),
        Hand([c['S9'], c['S8'], c['SQueen'], c['SJack'], c['S10']]),
        Hand([c['S9'], c['S8'], c['S7'], c['SJack'], c['S10']]),
        Hand([c['S9'], c['D9'], c['H9'], c['C9'], c['SJack']]),
        Hand([c['S9'], c['D9'], c['H9'], c['C9'], c['S4']]),
        Hand([c['S9'], c['D9'], c['HJack'], c['CJack'], c['SJack']]),
        Hand([c['S9'], c['D9'], c['H9'], c['CJack'], c['SJack']]),
        Hand([c['S9'], c['S3'], c['S5'], c['SQueen'], c['SJack']]),
        Hand([c['S9'], c['S3'], c['S2'], c['S5'], c['SJack']]),
        Hand([c['S9'], c['H8'], c['SQueen'], c['SJack'], c['S10']]),
        Hand([c['S9'], c['D2'], c['HJack'], c['CJack'], c['SJack']]),
        Hand([c['S5'], c['D2'], c['HJack'], c['CJack'], c['SJack']]),
        Hand([c['S9'], c['D9'], c['H9'], c['C8'], c['SJack']]),
        Hand([c['S5'], c['D2'], c['H6'], c['C8'], c['SJack']]),
        Hand([c['S5'], c['D2'], c['H9'], c['C10'], c['S4']])
    ]
    # Evaluate all hands to convert to PokerHand types
    for i, hand in enumerate(hands):
        hands[i] = hand.evaluate_poker()

    # For each hand, ensure all above win and all below loose.
    for i, hand in enumerate(hands):
        for j, test_hand in enumerate(hands):
            if i < j:
                assert hand > test_hand, f"[{hand} ({i})] should be better than [{test_hand} ({j})]."
            elif i > j:
                assert hand < test_hand, f"[{hand} ({i})] should be worse than [{test_hand} ({j})]."
            
    a = Hand([c['S9'], c['H8'], c['SQueen'], c['SJack'], c['S10']]).evaluate_poker()
    b = Hand([c['C8'], c['H10'], c['DQueen'], c['S9'], c['CJack']]).evaluate_poker()
    assert a == b, f"[{a}] should be equal to [{b}]."

    print("PokerHand Test Cases All Passed")

def straight_flush():
    """Ensure straight flush is detectable."""
    c = get_card_dict()
    h = Hand([c['S9'], c['S8'], c['SQueen'], c['SJack'], c['S10']])
    print(h.evaluate_poker())
    raise EndTest()


class EndTest(Exception):
    pass


if __name__ == "__main__":
    try:
        # straight_flush()
        test_cases()
        interactive_test()
    except EndTest:
        pass