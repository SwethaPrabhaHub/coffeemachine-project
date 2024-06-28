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


resources = {"water": 300,
             "milk": 200,
             "coffee": 100}

profit = 0

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def make_coffee(coffee_type, order_ing):
    for each_item in order_ing:
        resources[each_item] -= order_ing[each_item]
    print(f"Here is your {coffee_type}☕. Enjoy")


def item_level(items):
    for ing in items:
        if resources[ing] >= items[ing]:
            return True
        else:
            print(f"{ing} is not enough")
            return False


def process_coins():
    print("Insert coins :")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.10
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    print(total)
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        profit += money_received
        return True
    else:
        print("Sorry that's not enough money, Money refunded")


is_continue = True

while is_continue:
    user_request = input("What would you like to have?(espresso, latte, cappuccino):")
    if user_request == "off":
        is_continue = False
    elif user_request == "report":
        for item in resources:
            print(f"{item} : {resources[item]}ml")
    else:
        drink = MENU[user_request]
        if item_level(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_request, drink["ingredients"])

