from dataclasses import dataclass
import random
#suit names
suit_names = ["Joker","Hearts","Diamonds","Clubs","Spades"]
value_names = ["Nil","Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]

#card object
@dataclass
class Card():
    suit : int
    value : int
    
    def print_card_name(self):
        if self.value ==0:
            print(suit_names[self.suit])
        else:
            print(value_names[self.value]," of ",suit_names[self.suit])

#Deck object
class Deck():
    def __init__(self,num_packs : int, num_jokers : int):
        self.deck = []
        #add cards to the starting deck
        for i in range(num_jokers):
            self.deck.append(Card(0,0))
        for i in range(num_packs):
            for suit_val in range(1,len(suit_names)):
                for val_val in range(1,len(value_names)):
                    self.deck.append(Card(suit_val,val_val))
        random.shuffle(self.deck)    

    def print_deck(self):
        for card in self.deck:
            card.print_card_name()
    
    def deal(self,num_to_deal):
        dealt = []
        for i in range(num_to_deal):
            if len(self.deck)>0:
                dealt.append(self.deck.pop())
        return dealt
    
class Game():
    def __init__(self,players):
        self.players = players
        self.deck = Deck(2,4)
        



