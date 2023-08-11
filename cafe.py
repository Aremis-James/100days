cafe = {
    "espresso": dict(recipe=dict(water=50, coffee=18), cost=1.5),
    "latte": dict(recipe=dict(water=200, milk=150, coffee=24), cost=2.5),
    "cappuccino": dict(recipe=dict(water=250, milk=100, coffee=24), cost=3.0),
}

stock, profit = dict(water=300, milk=200, coffee=100), 0
menu = list(cafe.keys())


def report():
    """Generate a report on cafe inventory"""
    report_text = ""
    for item in stock:
        unit = "mL" if item in ["water", "milk"] else "G"
        report_text += f"{item.capitalize()}: {stock[item]}{unit}\n"
    report_text += f"Money: ${profit}"
    return report_text


def check_stock(s, d, c):
    """Check if there is enough stock to make a specific drink."""
    if d not in c:
        print("Invalid drink selection.")
        return False
    for x in c[d]["recipe"]:
        if s[x] < c[d]["recipe"][x]:
            print(f"Sorry there is not a enough {x}")
            return False
    return True


def coins():
    """Calculate the total amount of coins input by the user."""
    print("please insert coins")
    coin_value, total = dict(quarters=0.25, dimes=0.10, nickels=0.05, pennies=0.01), 0.0
    for coin in coin_value:
        while True:
            try:
                num_coins = float(input(f"How many {coin}?: "))
                if num_coins >= 0:
                    total += num_coins * coin_value[coin]
                    break
                else:
                    print("Please enter a non-negative value.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return total


def change(c):
    """Calculate and return the change to be given to the user after purchasing a drink."""
    amount = coins()
    sorry = f"Sorry that's not enough money for a {c}. ${amount} refunded."
    cup = f"Here is {round(amount - cafe[c]['cost'], 2)} in change.\nHere is your {c}☕️. Enjoy!"
    print(sorry if amount < cafe[c]["cost"] else cup)


no_cafe = False
while not no_cafe:
    choice = (
        input(f"What would you like? ({menu[0]},{menu[1]},{menu[2]})\n").strip().lower()
    )
    if choice == "off":
        no_cafe = True
    elif choice == "report":
        print(report())
    else:
        if check_stock(stock, choice, cafe):
            change(choice)
            profit += cafe[choice]["cost"]
            for ingredients in cafe[choice]["recipe"]:
                stock[ingredients] -= cafe[choice]["recipe"][ingredients]
