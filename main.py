# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 22:22:32 2022

@author: svenk
"""
from coffeemachine import CoffeeMachine
from money import Money

jura = CoffeeMachine('Jura X8')

selection = ''
resource_to_add = ''
recipe = {}
err = False
menu_choices = list(jura.MENU.keys())
menu_choices.extend(['off', 'add', 'coins'])
resources = list(jura.resources.keys())

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
        jura.acccept_coins()
        selection = ''

    else:
        print('You selected ', selection)

        for recipe_item, recipe_item_value in jura.MENU[selection]["ingredients"].items():
            if jura.resources[recipe_item]["amount"] < recipe_item_value:
                print(f'Not enough {recipe_item}. Please add.')
                selection = 'add'
                err = True
                break

        if not err:

            jura.accept_coins(jura.MENU[selection]["cost"])

            selection = ''
