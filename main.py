from oop_resaleshop import *

def main():

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Create shop, and assign to variable
    merrys_shop = ResaleShop()

    # Create New Computer with Computer class, and assign to variable.
    new_computer = Computer("Mac Pro (Late 2013)", 
                            "3.5 GHc 6-Core Intel Xeon E5", 
                            1024, 
                            64, 
                            "macOS Big Sur", 
                            2013, 
                            1500)
    
    # Add New Computer to the resale store's inventory with "buy" method.
    # Display New Computer's description. 
    print("Buying", new_computer.description)
    print("Adding to inventory...")
    merrys_shop.buy(new_computer)
    print("Done.\n")
    
    # Make sure New Computer was added to inventory. 
    #Check inventory by using "print inventory" method. 
    print("Checking inventory...")
    merrys_shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    #Assign updated operating system to variable. 
    new_OS = "MacOS Monterey"
    print("Refurbishing", new_computer.description, "- updating OS to", new_OS)
    #update OS and price with refurbish method
    print("Updating inventory...")
    merrys_shop.refurbish(new_OS)
    
    #Make sure it worked by checking inventory
    print("Checking inventory...")
    merrys_shop.print_inventory()
    print("Done.\n")

    # Now, let's sell it!
    print("Selling", new_computer.description)
    # Remove New Computer from inventory with "sell" method
    merrys_shop.sell(new_computer)

    #Make sure it worked by checking inventory
    print("Checking inventory...")
    merrys_shop.print_inventory()
    print("Done.\n")

if __name__ == "__main__":
    main()
    