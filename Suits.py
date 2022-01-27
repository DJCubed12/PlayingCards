"""Suit class and an instance for the 4 suits in cards. These instances are to be imported and used as constants. 
Prefered suit equivalence testing is with <Suit> is <Suit>, but <Suit> == <Suit> works too."""

class Suit:
    """Represents a playing card suit. Has a color attribute."""

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

Hearts = Suit("Hearts", "red")
Diamonds = Suit("Diamonds", "red")
Spades = Suit("Spades", "black")
Clubs = Suit("Clubs", "black")

all_suits = (Hearts, Diamonds, Spades, Clubs)


if __name__ == "__main__":
    # For testing
    for suit in (Hearts, Diamonds, Spades, Clubs):
        print(suit)

    assert Hearts != Diamonds
    assert Hearts is not Diamonds
    assert Spades != Diamonds
    assert Spades is not Diamonds

    assert Diamonds is Diamonds
    assert Diamonds == Diamonds