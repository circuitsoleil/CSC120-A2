#import computer class
from computer import *

class ResaleShop:

    def __init__(self):
        self.inventory = []
    
    def buy(self, computer):
        self.inventory.append(computer)

    def display_inventory(self): 
        for computer in self.inventory:
            print(computer)    
