


from typing import Dict, Union, Optional
from computer import 

itemID = 0 

class ResaleShop:
    

    inventory: Dict[int, Dict[str, Union[str, int, bool]]] = {}
    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = inventory 

        pass # You'll remove this when you fill out your constructor
    def print_inventory(self.inventory):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {inventory[item_id]}')
        else:
            print("No inventory to display.")

    # What methods will you need?
