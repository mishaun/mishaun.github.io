# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:12:02 2020

@author: mishaun
"""

import blackjack_classes
import random

choice = "" #variable for user to hit or stay
playing = True

#starting game - creating deck, dealer, and player
deck = Deck()
deck.shuffle()



player = Hand()
dealer = Hand()

#dealing cards to player and dealer
player.add_card(deck.deal())
dealer.add_card(deck.deal())
player.add_card(deck.deal())
dealer.add_card(deck.deal())

print("Player hand is: ")
player.show_hand()

print("Dealer is showing: ")
dealer.hand[0].show()
##############

while playing:
    
    if player.value == 21:
        print("You Win")
        break
    
    choice = input("Player: Hit or Stay? ").upper()
    
    if choice == "hit".upper():
        player.add_card(deck.deal())
        player.show_hand()
        
        if player.value > 21:
            print("You Busted - You Lose")
            break       
        
    elif choice == "stay".upper():
        
        if dealer.value > player.value:
            print("\nDealer wins - You Lose")
            print("\nDealer hand is: \n")
            dealer.show_hand()
            break
        else:
            while dealer.value<player.value:
                dealer.add_card(deck.deal())
                
            print("\nDealer hand is: ")
            dealer.show_hand()
            
            if dealer.value < 21:
                print("\nDealer Wins")
            else: 
                print("\nPlayer Wins - Dealer Busted")
            break
    

    





#############


#if player.value == 21:
#    print("You have reached 21, you win")
#else: 
#    while choice != "Stay".upper():
#        choice = input("Hit or Stay:  ").upper()
#        
#        if choice == "Hit".upper():
#            player.add_card(deck.deal())
#            print("Player hand is: ")
#            player.show_hand()
#            
#            if player.value > 21:
#                print("You Lose!")
#                break
#    
#
#if dealer.value > player.value:
#    print("Dealer Wins")
#    print("\nDealer's hand is: ")
#    dealer.show_hand()
#else:
#    while dealer.value < player.value:
#        dealer.add_card(deck.deal())
#        dealer.show_hand()
#        if dealer.value>21:
#            print("You Win")
#            break
#        
#        if dealer.value>player.value:
#            print("Dealer Wins")
#            break


            






