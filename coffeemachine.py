from money import Money

class CoffeeMachine():
    
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
        print(f'Cash balance remaining: ${self.money_balance():.2f}')    
            
            
    def money_balance(self):
        
        balance = 0
        for v in self.cash_register.coins.values():
            balance += v["value"] * v["count"]
        
        return balance
    

        
                
    def add_resource(self, resource, amount):
        
        self.resources[resource]["amount"] += amount
        
    def make_coffee(self, selection):
        
        pass
    

