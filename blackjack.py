import random
import os
from art import logo
"""
numbers count as face value. jack queen and king are ten. ace can be one towards total or 11, can decide
if over 21- bust, you lose
if dealer under 17, must play another card. 
if over 21, if have 11- change to 1
unlimited deck, no jokers
cards not removed from deck when used
"""
#function to deal new card
def deal_card():
    #returns random card from deck
    #11 is ace
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
#function to get sum of cards, and check for blackjack
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#function to compare scores at end of game
def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose"
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, opponent has a Blackjack"
    elif user_score == 0:
        return "Win, you got a Blackjack!"
    elif comp_score > 21 and user_score <21:
        return"Opponent went over. You win!"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"
#main game function
#starting hand, and lead to other functions    
def blackjack():
    print(logo)
    user_cards = []
    comp_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score >21:
            is_game_over = True
        else:
            should_deal = input("Type 'y' to get another card, 'n' to be done")
            if should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))  
#starting point, do you want to play yes or no
#and asked at end of game
while input("Do you want to play? 'y' for yes, 'n' for no:\n") == 'y':
    os.system('cls')
    blackjack()