import random
from art import logo #2nd to last step of project



def deal_card():
    #returns  a random card from deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
#ace = 11
#10s = jack, queen, king
# every "card" has equal chance of winning

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)  # this adds the card list

#this function was made later on in code not in beginning
#neeed to make sure variable names in this function are not the same name as other variables/lists in code
def compare(u_score, c_score): #cannot call for a function if it is not created, you should not create functions in while loop usually
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has blackjack"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃" #remember you are the user try to be concise and in position of user
    else:
        return "You lose 😤"
def play_game():
    print(logo) #very last step was adding this
    user_cards = []
    user_score = -1  # to let the 2nd while loop run because just in user_score has no score and cannot be defined when while loop is run
    computer_cards = []
    computer_score = -1  # this needs to be defined to just let the 2nd while loop run
    is_game_over = False

    for _ in range(2):  # one card for dealer and one for user
        user_card.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:  # this while loop is for user to keep taking cards
        # this part of code solves checks the scores of the user and computer
        user_score = calculate_score(
            user_cards)  # calls the calculate score function and puts user cards list as input and saves it as variable
        calculate_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}"

        # this part of the code checks the if's of the data obtained
        if user_score == 0 or calculate_score == 0 or user_score > 21:      # checks if blackjack or user score is over 21
            is_game_over = True
        else:
            user_should_deal = input("Type 'y to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:  # for computer so that dealer can follow their strategy
        computer_cards.append(deal_card())  # deals another card
        computer_score = calculate_score(
            computer_cards)  # recalculate computer score by putting a function output within a function

    print(
        f"Your final hand: {user_cards}, final score: {user_score}")  # shows user more information about the hand and their score
    print(
        f"Computer final hand: {computer_cards}, final score: {computer_score}")  # then reveal to user the computer's score
    print(compare(computer_score, user_score))  # first time using compare function

    while input("Do you want to play again? Type 'y' or n: ") == "y": #this will continue game and you must now make the play_game function, while this continues it will keep having chance to play game until user says no
        print("/n" * 20)
        play_game()

calculate_score(user_cards)

