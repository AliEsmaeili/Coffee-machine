# Write your code here
coffee_preparation_message = """Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!"""


class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9
    coffees = {"1": ("espresso", 250, 0, 16, 4),
               "2": ("latte", 350, 75, 20, 7),
               "3": ("cappuccino", 200, 100, 12, 6)}
    coffee_menu = {number: {"name": coffee[0], "water": coffee[1], "milk": coffee[2], "beans": coffee[3], "cost": coffee[4]} for number, coffee in coffees.items()}
    supplies = ("ml of water", "ml of milk", "grams of coffee beans", "disposable cups of coffee")

    @staticmethod
    def start_action():
        print("Write action (buy, fill, take, remaining, exit):")

    def __init__(self):
        self.supply = []
        self.prepare = False

    def fill(self, index):
        print(f"Write how many {self.supplies[index]} do you want to add:")

    def start_buy(self):
        self.prepare = True
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

    def remaining(self):
        print(f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.cups} of disposable cups
{self.money} $ of money""")
        self.start_action()

    def take(self):
        print(f"I gave you {self.money} $")
        self.money = 0
        self.start_action()

    def buy(self, coffee_number):
        coffee = self.coffee_menu.get(coffee_number)
        if coffee:
            self.prepare = False
            left = {"water": self.water,
                    "milk": self.milk,
                    "beans": self.beans,
                    "cups": self.cups}
            low_items = [key for key, value in left.items() if coffee.get(key, 1) and value // coffee.get(key, 1) == 0]
            if low_items:
                print("Sorry, not enough", " and ".join(low_items), "!")
            else:
                print(coffee_preparation_message)
                self.money += coffee["cost"]
                self.water -= coffee["water"]
                self.milk -= coffee["milk"]
                self.beans -= coffee["beans"]
                self.cups -= 1
        else:
            self.start_buy()

    def main(self, order):
        if self.supply:
            if len(self.supply) == 4:
                self.supply.append(int(order))
                self.water += self.supply[1]
                self.milk += self.supply[2]
                self.beans += self.supply[3]
                self.cups += self.supply[4]
                self.supply = []
                self.start_action()
            else:
                self.fill(len(self.supply))
                self.supply.append(int(order))
        elif self.prepare:
            if order != "back":
                self.buy(order)
            else:
                self.prepare = False
                self.start_action()
        elif order == "buy":
            self.start_buy()
        elif order == "remaining":
            self.remaining()
        elif order == "fill":
            self.supply.append(None)
            self.fill(0)
        elif order == 'take':
            self.take()
        else:
            self.start_action()


coffee_machine = CoffeeMachine()
action = input("Write action (buy, fill, take, remaining, exit):")
while action != "exit":
    coffee_machine.main(action)
    action = input()
