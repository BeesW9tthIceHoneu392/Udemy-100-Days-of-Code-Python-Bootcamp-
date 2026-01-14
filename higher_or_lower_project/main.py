#final if statemnt does not need to be inside a function to finish the game --->reason for this is so we can escape the while loop by using the if statemnt while checking the score

# format random choice & make into a function  & functions should be defined at beggining of a project/problem
# any repeatable code should be made into a function
def format_random_choice(account):
    account_name = account["name"]
    followers = account["follower_count"]
    descrip = account["description"]
    country_origin = account["country"]
    return (f"{account_name}, {followers}, {descrip}, {country_origin}")

#the function called check answer was made way in the middle of the project and was added to the top later on
def check_answer(user_guess, a_followers, b_followers):
    "Take a account followers and b account followers and compare which one is higher"
    if a_followers > b_followers: #basically first check which answer is higher & then return that answer
        return user_guess == "a" #very simple way to make long line of if and statements of code into smaller bits
    else:
        if b_followers > a_followers:
            return user_guess == "b"

# print logo, vs, & import data
from art import logo, vs
from game_data import data
import random
score = 0
game_should_continue = True
account_B = random.choice(data)

while game_should_continue:

    # generate random choice from data dictionary
    account_A = random.choice(data)
    account_B = random.choice(data)

    if account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_random_choice(account_A)}.")
    print(vs)
    print(f"Against B: {format_random_choice(account_B)}.")

    # ask user who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # check which choice has higher followers
    a_followers_account = account_A["follower_count"]
    b_followers_account = account_B["follower_count"]

    is_correct = check_answer(guess, a_followers_account, b_followers_account)#stores answers of check answer function into a variable


    #giver user feedback & add 1 to score everytime you are right &
    if is_correct:
        score += 1
        print("Correct! Current score {score}")
    else:
        print("Incorrect! Final score {score}.")
        game_should_continue = False



## ask to guess again everytime you are right (while loop) ---> once at this step figure out where to put while loop i.e. what parts of the code above need to be repeated

# end function (the game) once you guess wrong
