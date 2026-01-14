MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



# COFFEE MACHINE PROJECT
# TODO 1. Print Report
# TODO 2. Check resources sufficent to make drink order.
# TODO 3. Process Coins
# TODO 4. Check Transaction succesful?
# TODO 5. Make Coffee

def is_resource_sufficent(order_ingredients): #order_ingredients is just an input not real variable the actual input you will use is this:  if is_resource_sufficent(drink["ingredients"])
    "Returns true when order can be made and false when not enough resources"
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]: #can use key twice here and it matches ingredients in resources and order_ingredients
            print(f"Sorry there is not enough {item}.")
            return False #need a way to end for loop
    return True #keeps going

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_succesful(money_received, drink_cost)
   if money_received >= drink_cost:
       return True
   else:
       print(f"Sorry there is not enough money! Money refunded.")
       return False #false needs to be here and not above because false ends the function




#this is the actual functionality of the coffee machine and above is just the functions and global varaibles
is_on = True

while True:
    choice = input("What would you like? (espresso, latte, cappuccino):  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficent(drink["ingredients"]): #if there are enough resources then we ask for money
            payment = process_coins()










def check_resources(drink_types)
    for items in resources:
        if items >
