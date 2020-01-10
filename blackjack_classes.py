# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:06:59 2020

@author: mishaun
"""

'''
This script will hold all the classes required for the blackjack game'
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def show(self):
        print(f'{self.rank} of {self.suit}')

class Deck:
    
    def __init__(self):
        #emtpy list that will be appended with list of card objects
        self.deck = []
        self.build() #running building of deck upon instanciation
        self.shuffle()
        
    def build(self):
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)
    
    def show(self):
        for c in self.deck:
            c.show()
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop(0)
        return single_card

class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.hand.append(card)
        self.value += card.value
        
        if card.rank == "Ace":
            self.aces +=1
        
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
        
    def show_hand(self):
        for card in self.hand:
            card.show()
        
        print(f"Hand value is: {self.value}\n")
    def reset_hand(self):
        self.hand = []
        self.value = 0
        
class Chips:
    def __init__(self, worth = 100):
        self.worth = worth
        
    def bet(self,amount):
        self.worth -= amount
    
    def win(self, winnings):
        self.worth+=winnings*2
    def __str__(self):
        return "Player chips balance: {}".format(self.worth)

#############################



    
    
    