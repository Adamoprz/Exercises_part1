import random

class Card:
    def __init__(self, value, figure):
        self.figure = figure
        self.value = value
    def str(self):
        return ("{} - {}".format(self.value, self.figure))

    def describe_card(self):
        print("{} - {}".format(self.value, self.figure))


class Deck:
    def __init__(self, figures, values):
        self.card = []
        self.figures = figures
        self.values = values
        for value in values:
            for figure in figures:
                t = Card(value, figure)
                self.card.append(t.str)

    def shuffle(self):
        return random.shuffle(cards)
    def deal(self):
        pass


def main():
    figures = ["Diamond", "Clubs", "Heart", "Spade"]
    values = ["A", 2, 3, 4, 5, 6, 7, 8, 10, "J" , "Q" , "K"]
    talia = Deck(figures, values)

if __name__ == "__main__":
    main()