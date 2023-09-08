import random
import art
import os

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """take a list of cards and return the sum of cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You Lose"
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return "You lose and the opponent has a blackjack"
    elif user_score == 0:
        return "You win ! Blackjack."
    elif user_score > 21:
        return "You went over. You Lose"
    elif computer_score > 21:
        return "You won! Dealer went over"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You Lost!"
def play_game():
    player_name = input("Enter Your Name : ").title()
    print(art.logo)
    print(f"Welcome to the game of BlackJack : {player_name}.")
    is_game_over = False
    user_cards = []
    computer_cards= []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"{player_name}'s cards : {user_cards}, Current Score: {user_score}")
        print(f"Dealer's First Card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type Y to get another card or Type N to Pass : ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over= True

    while computer_score != 0 and computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
    print(f"Your final hand : {user_cards}, Final Score : {user_score}")
    print(f"Delaer's Final Hand : {computer_cards}, Dealer's Score : {computer_score}")
    print(compare_score(user_score, computer_score))

    while input("Do you want a rematch ?").lower() == 'y':
        clear_screen()
        play_game()
play_game()





