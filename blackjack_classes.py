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

class Player:
    
    def __init__(self, chips = 100):
        pass
    
    