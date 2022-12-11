# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:59:33 2022

@author: svenk
"""

class Money():
    
    def __init__(self):
        self.coins = {"quarters": {
            "value": 25,
            "count": 0
            },
        "dimes": {
            "value": 10,
            "count": 0
            },
        "nickles": {
            "value": 5,
            "count": 0
            },
        "pennies": {
            "value": 1,
            "count": 0
            },
        }
    
    def add(self, other):
        
        for v in self.coins.keys():
            self.coins[v]["count"] += other.coins[v]["count"]
        
        return self
    
    def reduce(self, other):
        
        for v in self.coins.keys():
            self.coins[v]["count"] -= other.coins[v]["count"]
        
        return self
    
    def value(self):
        
        sum = 0
        for v in self.coins.values():
            sum += v["value"] * v["count"]
        
        return sum
    
    def __repr__(self):
        
        return str(self.coins)

     

