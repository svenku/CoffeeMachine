# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 22:22:32 2022

@author: svenk
"""
from coffeemachine import CoffeeMachine
from money import Money

jura = CoffeeMachine('Jura X8')
user_cash = Money()
selection = ''
resource_to_add = ''
recipe = {}
err = False
menu_choices = list(jura.MENU.keys())
menu_choices.extend(['off', 'add', 'coins'])
resources = list(jura.resources.keys())

def enter_coins(required_amount):
    
    while user_cash.value() < required_amount*100:
        for v in user_cash.coins.keys():
            user_cash.coins[v]["count"] += int(input('Enter number of ' + v + " you are entering: "))
            print(f'Entered: ${user_cash.value()/100:.2f} Remaining: ${required_amount - user_cash.value()/100:.2f}')


print(menu_choices)



while True:
    
    jura.report()
    
    while selection not in menu_choices:
        selection = input('What would you like? (espresso/latte/cappuccino): ')
        
    if selection == 'off':
        print('Switching off....')
        break
    
    elif selection == 'add':
        while resource_to_add not in resources:
            resource_to_add = input('What would you like to add? (water/coffee/milk): ')
        amt = int(input('Enter amount: '))
        jura.add_resource(resource_to_add, amt)
        resource_to_add = ''
        amt = 0
        selection = ''
    
    elif selection == 'coins':
        jura.enter_coins()
        selection = ''
    
    else:
        print('You selected ', selection)
        
        for recipe_item, recipe_item_value in jura.MENU[selection]["ingredients"].items():
            if jura.resources[recipe_item]["amount"]<recipe_item_value:
                print(f'Not enough {recipe_item}. Please add.')
                selection = 'add'
                err = True
                break
        
        if not err:
            print(f'Your selected drink costs: ${jura.MENU[selection]["cost"]}')
            print('Please enter appropriate amount of coins.')
            enter_coins(jura.MENU[selection]["cost"])
            jura.make_coffee(selection)
            selection = ''
        
        