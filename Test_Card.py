from Card import Card
from Suits import Hearts, Diamonds, Spades, Clubs


def test_sequence():
    """Runs all tests."""
    str_test()
    comparison_test()
    and_or_test()


def str_test():
    samples = {
        "2 of Diamonds": Card(2, Diamonds),
        "10 of Spades": Card(10, Spades),
        "Jack of Hearts": Card(11, Hearts),
        "Queen of Clubs": Card(12, Clubs),
        "King of Diamonds": Card(13, Diamonds),
        "Ace of Spades": Card(14, Spades)
    }

    for key, card in samples.items():
        out = str(card)
        assert key == out, f'{card.value} of {str(card.suit)} returned "{out}".'

    print("String Conversion Test Passed")

def comparison_test():
    samples = {
        2: Card(2, Diamonds),
        5: Card(5, Spades),
        8: Card(8, Hearts),
        10: Card(10, Spades),
        13: Card(13, Diamonds),
        14: Card(14, Spades)
    }
    C_10 = Card(10, Clubs)

    assert (a := samples[13]) < (b := samples[14]), f"{a} should be < {b}."
    assert not((a := samples[10]) < (b := samples[2])), f"{a} should not be < {b}."
    assert not((a := samples[10]) < C_10), f"{a} should not be < {C_10}."

    assert (a := samples[13]) <= (b := samples[14]), f"{a} should be <= {b}."
    assert not((a := samples[10]) <= (b := samples[2])), f"{a} should not be <= {b}."
    assert (a := samples[10]) <= C_10, f"{a} should be <= {C_10}."

    assert (a := samples[8]) > (b := samples[5]), f"{a} should be > {b}."
    assert not((a := samples[2]) > (b := samples[5])), f"{a} should not be > {b}."
    assert not((a := samples[10]) > C_10), f"{a} should not be > {C_10}."

    assert (a := samples[8]) >= (b := samples[5]), f"{a} should be >= {b}."
    assert not((a := samples[2]) >= (b := samples[5])), f"{a} should not be >= {b}."
    assert (a := samples[10]) >= C_10, f"{a} should be >= {C_10}."

    assert (a := samples[10]) == C_10, f"{a} should be == {C_10}."
    assert not((a := samples[10]) == (b := samples[2])), f"{a} should not be == {b}."

    assert not((a := samples[10]) != C_10), f"{a} should not be != {C_10}."
    assert (a := samples[10]) != (b := samples[2]), f"{a} should be != {b}."

    print("Comparison Tests Passed")

def and_or_test():
    A = Card(10, Clubs)
    B = Card(10, Clubs)
    C = Card(6, Clubs)
    D = Card(10, Hearts)

    assert A & B, f"{A} should be the same as {B}"
    assert not(A & C), f"{A} should not be the same as {C}"
    assert not(A & D), f"{A} should not be the same as {D}"

    assert A | B, f"{A} should be suited with {B}"
    assert A | C, f"{A} should be suited with {C}"
    assert not(A | D), f"{A} should not be suited with {D}"

    print("And/Or Override Test Passed")


if __name__ == "__main__":
    test_sequence()