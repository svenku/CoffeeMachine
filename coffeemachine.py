from money import Money


class CoffeeMachine:
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
        "water": {
            "amount": 300,
            "unit": "ml"
        },
        "milk": {
            "amount": 200,
            "unit": "ml"
        },
        "coffee": {
            "amount": 100,
            "unit": "g"
        },
    }

    cash_register = Money()

    def __init__(self, name):
        self.name = name

    def report(self):
        print(self.name + ' ingredients remaining:')
        for k, v in self.resources.items():
            print(f'{k:>6} : {str(v["amount"]):>8}{v["unit"]}')
        print(f'Cash balance remaining: ${self.cash_register.value() / 100:.2f}')

    def get_change(self, amount):
        change = Money()
        for denomination in sorted(self.cash_register.coins.keys(), reverse=True):
            while denomination <= amount and self.cash_register.coins[denomination]['count'] > 0:
                amount -= denomination
                self.cash_register.coins[denomination]['count'] -= 1
                change.coins[denomination]['count'] += 1

        if amount != 0:
            raise Exception("Insufficient coins to give change")

        return change

    def accept_coins(self, required_amount):
        print(f'Your selected drink costs: ${required_amount}')
        print('Please enter appropriate amount of coins.')
        user_cash = Money()

        while user_cash.value() < required_amount * 100:
            for k in user_cash.coins.keys():
                user_cash.coins[k]["count"] += \
                    int(input(f'Enter number of {user_cash.coins[k]["name"]} ({k} cent coin) you are entering: '))

                remaining = required_amount * 100 - user_cash.value()

                if remaining > 0:
                    print(
                        f'Entered: ${user_cash.value() / 100:.2f} Remaining: ${remaining / 100:.2f}')

                elif remaining == 0:
                    self.cash_register.add(user_cash)
                    break

                else:
                    print(
                        f'Entered: ${user_cash.value() / 100:.2f} Returning change: ${-remaining / 100:.2f}')
                    self.cash_register.add(user_cash)
                    change_togive = self.get_change(-remaining)
                    print(f'Returning: {change_togive}')
                    break

    # def money_balance(self):
    #
    #     balance = 0
    #     for v in self.cash_register.coins.values():
    #         balance += v["value"] * v["count"]
    #
    #     return balance

    def add_resource(self, resource, amount):

        self.resources[resource]["amount"] += amount

    def make_coffee(self, selection):

        pass
