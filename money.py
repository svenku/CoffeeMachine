# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:59:33 2022

@author: svenk
"""


class Money:

    def __init__(self):
        self.coins = {
            25: {
                "name": "quarters",
                "count": 0
            },
            10: {
                "name": "dimes",
                "count": 0
            },
            5: {
                "name": "nickels",
                "count": 0
            },
            1: {
                "name": "pennies",
                "count": 0
            },
        }

    def add(self, other):

        for k in self.coins.keys():
            self.coins[k]["count"] += other.coins[k]["count"]

        return self

    def reduce(self, other):

        for k in self.coins.keys():
            self.coins[k]["count"] -= other.coins[k]["count"]

        return self

    def value(self):

        sum = 0
        for k in self.coins.keys():
            sum += k * str(k)["count"]

        return sum

    def __repr__(self):

        return str(self.coins)
