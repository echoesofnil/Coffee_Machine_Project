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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    """Check if enough resources are available"""
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def process_coins():
    """Calculate total money inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25 +
             dimes * 0.10 +
             nickles * 0.05 +
             pennies * 0.01)
    return total


def make_coffee(drink):
    """Deduct ingredients and serve coffee"""
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy! ☕")


def coffee_machine():
    profit = 0
    is_on = True

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Profit: ${profit}")

        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                cost = MENU[choice]["cost"]

                if payment >= cost:
                    change = round(payment - cost, 2)
                    profit += cost
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    make_coffee(choice)
                else:
                    print("Sorry, that's not enough money. Money refunded.")

        else:
            print("Invalid choice. Please select espresso, latte, or cappuccino.")

coffee_machine()
