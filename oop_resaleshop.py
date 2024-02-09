from computer import *

class ResaleShop:
    
    #attribute of Resale Shop
    inventory:list 

    #initialize empty list
    def __init__(self):
        self.inventory = [] 
    
    #add computer to inventory 
    def buy(self,computer):
        self.inventory.append(computer)
    
    def print_inventory(self): 
        #if inventory is not empty 
        if len(self.inventory) > 0: 
        #for the amount of attributes in inventory 
        #print attributes 
            for product in self.inventory:
                print(product.description,"\n",
                    product.processor_type,"\n","Hard Drive:",
                    product.hard_drive_capacity,"\n","Memory:",
                    product.computer_memory,"\n","OS:",
                    product.operating_system,"\n","Year:",
                    product.year_made,"\n","Price:",
                    product.price)
        else: 
            print("You have no items in your inventory!")

    def sell(self, computer): 
        if len(self.inventory) > 0:
            self.inventory.remove(computer)
    
    def refurbish(self, new_OS):
        #use methods from computer class 
        #run computer through conditional statements based on its attributes
        for product in self.inventory:
            if product.year_made < 2000:
                product.price = 0 #too old to sell, donation only
            elif product.year_made < 2012: 
                product.price = 250 #heavily-discounted price on machines 10+ years old
            elif product.year_made < 2018: 
                product.price = 550
            else:
                product.price = 1000 #recent stuff
        if new_OS is not None:
            product.operating_system = new_OS # update details after installing new OS
        else:
            print("Item", product.description, "not found. Please select another item to refurbish.")
            