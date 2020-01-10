# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:12:02 2020

@author: mishaun
"""
import blackjack_classes as bj

#initializing class objects
playing = True
stash = bj.Chips() #instanciating chips class for player
deck_of_cards = bj.Deck()
mishaun_player = bj.Hand()
dealer_hand = bj.Hand()

def start(player,dealer, deck, chips):
    #starting game - creating deck, dealer, and player
    
    bet_amount = int(input("Please enter your bet amount: "))
    chips.bet(bet_amount)
    
    #dealing cards to player and dealer
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
    print("Player hand is: ")
    player.show_hand()
    
    print("Dealer is showing: ")
    dealer.hand[0].show()
    
    return bet_amount
    ##############
    
def game_logic(player,dealer, deck, chips, bet_amount):
    while True:
        #Game Logic
        if player.value == 21:
            print("You Win")
            chips.win(bet_amount)
            break
        
        choice = "" #variable for user to hit or stay
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
                
                if dealer.value <= 21:
                    print("\nDealer Wins")
                else: 
                    print("\nPlayer Wins - Dealer Busted")
                    chips.win(bet_amount)
                break
        #game logic ends

while playing:
    
    Bet = start(mishaun_player, dealer_hand, deck_of_cards, stash)
    game_logic(mishaun_player, dealer_hand, deck_of_cards, stash, Bet)
    
    ask = input("Keep playing: Y/N  ").upper()
    
    if ask == 'y'.upper():
        dealer_hand.reset_hand()
        mishaun_player.reset_hand()
        continue
    else:
        print(stash)
        playing = False
    




            






