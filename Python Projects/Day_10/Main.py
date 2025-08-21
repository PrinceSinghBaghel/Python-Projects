Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25.50,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30.0,
    }
}

profit=0
resource = {"water":300,"milk":200,"coffee":100}

def resource_check(order_ingredients):
    """Returns True when order can be made, False if not"""
    for item in order_ingredients:
        if order_ingredients[item]>=resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coin inserted"""
    print("please insert coin.")
    total = int(input("How many 1 rupees?: "))*1
    total += int(input("How many 2 rupees?: "))*2
    total += int(input("How many 5 rupees?: "))*5
    total += int(input("How many 10 rupees?: "))*10
    return total

def transaction(money_recieved, drink_cost):
    """Return the payment details"""
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"Here is your change in Rs.{change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resource[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} 🍵")

#TODO: 1. Print report of all coffee machine resources
machine=True
while machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice=="off":
        machine=False
    elif choice=="report":
        print(f"Water: {resource['water']}ml")
        print(f"milk: {resource['milk']}ml")
        print(f"coffee: {resource['coffee']}gm")
        print(f"Money: Rs.{profit}")
    else:
        drink=Menu[choice]
        if resource_check(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
