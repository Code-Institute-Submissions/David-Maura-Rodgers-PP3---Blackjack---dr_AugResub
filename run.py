# TO RUN CODE: python3 run.py
import random
import sys
import os

# Hold random cards and the value of each hand
player_cards = []
com_cards = []
player_hand = 0
com_hand = 0

# Value of bets entered
# Betting over and round over conditions
START_BET = 30
BET_20 = 20
BET_40 = 40
BET_80 = 80
player_bet = 0
dealer_bet = 0
betting_over = False
round_over = False

# Calculate: add or subtract these variables after each bet to trigger
# end game conditions
round_pot = 0
player_pot = 1000
dealer_pot = 1000

# Check end game condition
is_game_over = False


print("""
----------- Blackjack House Rules ----------- \n
The Winner of each round is the player who hits 21 in their hand \
or as close to 21 as possible
Blackjack is awarded if you or the dealer have 21 with only 2 cards
You can be dealt as many cards as you like until you exceed 21. \
You will go bust and lose the round if this happens
Dealer will keep dealing cards for themself as long as their \
total value is less than 17
Both player and dealer start the game with €1,000
All bets start at €30 by default
The dealer will always match your bet should you chose to raise
The game is over when either the player or dealer pot (money) \
goes below €0 \n
""")


def random_card():
    '''
    FUNCTION: Will loop through available cards
    and then return a randomly selected one from the list
    '''
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(all_cards)
    return chosen_card


def place_bet():
    '''
    FUNCTION: Ask player to place bet from 3 options: 20, 40, 80
    Dealer will match this bet and both bets are added to the pot
    for that round
    '''
    player_bet = 0
    dealer_bet = 0
    global round_pot

    print("All players must bet €30 at the start of of every round.\n")

    while True:
        should_bet = input("Would you like to raise the bet? \nType 'y' for yes, \
or type 'n' to stay with your current bet of €30: \n")
        if should_bet.lower() == "n":
            player_bet = START_BET
            dealer_bet = START_BET
            round_pot = 60
            print(f"   Player bet this hand: €{player_bet}")
            print(f"   Dealer bet this hand: €{dealer_bet}")
            print(f"   Pot for this round is €{round_pot}")
            print("\n")
            play_game()
        elif should_bet.lower() == "y":
            calculate_bet()
        else:
            print("\n")
            print("Invalid Input: Please type either 'y' or 'n'")
            print("\n")


def calculate_bet():
    '''
    FUNCTION: Ask player to place bet from 3 options: 20, 40, 80
    Dealer will match this bet and both bets are added to the pot,
    for that round
    '''
    global betting_over
    player_bet = 0
    dealer_bet = 0
    global round_pot

    try:
        print("\n")
        add_bet = int(input("Please enter bet: 20, 40 or 80: \n"))

        if add_bet == 20:
            player_bet = BET_20 + START_BET
            dealer_bet = player_bet
            round_pot = 100
            print(f"    Player bet this hand: €{player_bet}")
            print(f"    Dealer bet this hand: €{dealer_bet}")
            print(f"    Pot for this round is €{round_pot}\n")
            betting_over = True
            play_game()

        elif add_bet == 40:
            player_bet = BET_40 + START_BET
            dealer_bet = player_bet
            round_pot = 140
            print(f"    Player bet this hand: €{player_bet}")
            print(f"    Dealer bet this hand: €{dealer_bet}")
            print(f"    Pot for this round is €{round_pot}\n")
            betting_over = True
            play_game()

        elif add_bet == 80:
            player_bet = BET_80 + START_BET
            dealer_bet = player_bet
            round_pot = 220
            print(f"    Player bet this hand: €{player_bet}")
            print(f"    Dealer bet this hand: €{dealer_bet}")
            print(f"    Pot for this round is €{round_pot}\n")
            betting_over = True
            play_game()

        else:
            print("Incorrect amount: please select 20, 40 or 80")
            print("\n")

    except Exception:
        print("\n")
        print("Invalid Input: Please enter a number")
        print("\n")
        calculate_bet()


def calculate_card_sum(all_cards):
    '''
    FUNCTION: check for a Blackjack:
    a hand with only 2 cards: ace + 10, and return 0
    Take list of both hands (player and com)
    and return the sum of those cards
    '''
    # Check for a blackjack (a hand with only 2 cards: ace + 10)
    # and return 0 instead of the actual score
    # 0 represents a blackjack
    if sum(all_cards) == 21 and len(all_cards) == 2:
        return 0
    # Check for an 11 (ace). If the score is already over 21,
    # remove the 11 and replace it with a 1.
    if 11 in all_cards and sum(all_cards) > 21:
        all_cards.remove(11)
        all_cards.append(1)
    return sum(all_cards)


def return_winner(p_hand, c_hand):
    '''
    FUNCTION: Compare values of player hand and com hand and determine
    the winner
    '''
    winner = ""
    if p_hand == c_hand:
        print("\n")
        print("This round is a draw . . .\n")
    elif c_hand == 0:
        winner = "Dealer"
        print("\n")
        print("You lose - dealer has Blackjack 😱\n")
    elif p_hand == 0:
        winner = "Player"
        print("\n")
        print("You Win - with a Blackjack 😎\n")
    elif p_hand > 21:
        winner = "Dealer"
        print("\n")
        print("You went over. You lose 😭\n")
    elif c_hand > 21:
        winner = "Player"
        print("\n")
        print("Opponent went over. You win 😁\n")
    elif p_hand > c_hand:
        winner = "Player"
        print("\n")
        print("You win 😃\n")
    else:
        winner = "Dealer"
        print("\n")
        print("You lose 😤\n")
    return winner


def play_again():
    """
    Player can decide if they want to play
    a new game or exit it.
    """
    global player_pot
    global dealer_pot

    while True:
        try_again = input("Would you like to play again? \
Please enter either 'y' or 'n': \n")
        if try_again.lower() == 'y':
            player_pot = 1000
            dealer_pot = 1000
            start_game()
            break
        elif try_again.lower() == 'n':
            os.system('cls||clear')
            print("Thanks for playing. Hopefully see you soon")
            sys.exit()
            break
        else:
            print("Invalid Input: Please enter either Y or N")


def play_game():
    '''
    FUNCTION:
    Will start the game - Deal random cards into player's and dealer's hands
    Check conditions to find the winner of the round
    Check for end game condition to determine the winner
    '''
    player_cards = []
    com_cards = []
    player_hand = 0
    com_hand = 0
    the_winner = ""
    round_over = False
    is_game_over = False
    global round_pot
    global player_pot
    global dealer_pot

    print(f"    Player Pot is currently: €{player_pot}")
    print(f"    Dealer Pot is currently: €{dealer_pot}")
    print("\n")
    for card in range(2):
        player_cards.append(random_card())
        com_cards.append(random_card())

    while not round_over:
        player_hand = calculate_card_sum(player_cards)
        com_hand = calculate_card_sum(com_cards)
        print(f"Dealer's first card is: {com_cards[0]}\n")
        print(f"Your hand: {player_cards} current score: {player_hand}\n")
        if player_hand == 0 or com_hand == 0 or player_hand > 21:
            round_over = True
            os.system('cls||clear')
        else:
            while True:
                player_deal_again = input("Type 'y' to deal another card \
or 'n' to stick with your current hand: \n")

                if player_deal_again.lower() == "y":
                    player_cards.append(random_card())
                    print("\n")
                    print(
                        f"Dealer's hand: {com_cards} score: {com_hand}"
                        )
                    break
                elif player_deal_again.lower() == "n":
                    round_over = True
                    os.system('cls||clear')
                    break
                else:
                    print("Invalid Input: Please enter either 'y' or 'n'")
                    print("\n")

    # Loop to ensure that the dealer will be dealt a card while their
    # score is less than 17
    while com_hand != 0 and com_hand < 17:
        com_cards.append(random_card())
        com_hand = calculate_card_sum(com_cards)

    print(f"Your final hand: {player_cards}, final score: {player_hand}")
    print(f"Computer's final hand: {com_cards}, final score: {com_hand}")

    the_winner = return_winner(player_hand, com_hand)
    print(f"THE WINNER: {the_winner}")

    if the_winner == "Player":
        player_pot = player_pot + round_pot
        dealer_pot = dealer_pot - round_pot
    if the_winner == "Dealer":
        player_pot = player_pot - round_pot
        dealer_pot = dealer_pot + round_pot
    print(f"Player Pot is now: €{player_pot}")
    print(f"Dealer Pot is now: €{dealer_pot}")
    print("\n")

    round_pot = 0

    while not is_game_over:
        if player_pot >= 1 and dealer_pot >= 1:
            place_bet()
            calculate_bet()
            play_game()

        elif player_pot <= 0:
            print("Your pot is empty")
            print("GAME OVER: You lose . . . .\n")
            is_game_over = True
            play_again()

        elif dealer_pot <= 0:
            print("Dealer pot is empty!!!")
            print("GAME OVER: You WIN!!!!!!\n")
            is_game_over = True
            play_again()


# Ask the player if they want to play another round
# Will end the game if user selects 'N'
def start_game():
    '''
    Function: Choose to start a new game
    when app launches
    '''
    global player_cards
    global com_cards

    while True:
        ready = input("Would you like to start a new game of Blackjack? \
Please type 'y' to continue or 'n' to exit: \n")
        if ready.lower() == 'y':
            print("\n")
            os.system('cls||clear')
            player_cards = []
            com_cards = []
            place_bet()
            calculate_bet()
            play_game()
            break
        elif ready.lower() == 'n':
            print("\n")
            print("Goodbye. Hopefully see you soon!")
            break
        else:
            print("Invalid Input: Please enter either 'y' or 'n'")
            print("\n")


start_game()
