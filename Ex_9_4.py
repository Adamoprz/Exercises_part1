import random

class Card:
    def __init__(self, value:str, figure:str) -> None:
        self.figure = figure
        self.value = value
    def return_card(self) -> str:
        return f"{self.value} - {self.figure}"


class Deck:
    def __init__(self, figures:list, values:list) -> None:
        self.card_ = []
        self.figures = figures
        self.values = values

    def create_Deck(self) -> None:
        for value in self.values:
            for figure in self.figures:
                t = Card(value, figure)
                self.add(t.return_card())

    def add(self, added_card: str) -> None:
        self.card_.append(added_card)

    def shuffle(self) -> None:
        random.shuffle(self.card_)

    def deal(self) -> str:
        temp = self.card_[-1]
        self.card_=self.card_[:-1]
        return temp

def main():
    figures = ["Diamond", "Clubs", "Heart", "Spade"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "10", "J" , "Q" , "K"]
    #Generate and create new deck
    deck_f = Deck(figures, values)
    deck_f.create_Deck()
    #print all cards of the deck
    print(deck_f.card_)
    #shuffle deck
    deck_f.shuffle()
    #print shuffled deck
    print(deck_f.card_)
    #print last card from the shuffled deck and remove the last card from deck.
    print(deck_f.deal())
    #print deck (now it is reduced by one card
    print(deck_f.card_)

if __name__ == "__main__":
    main()