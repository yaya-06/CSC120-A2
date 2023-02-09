"""oo_resale_shop.py: Creates a resale shop class and has selling, buying, and inventory checking methods."""

__author__      = "Yaya Callahan"

from computer import * 

class ResaleShop:
    
    
    inventory = []
    #name: str
    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.itemID = 0
    
    def buy(self, computer):
        self.inventory.append(computer)

    def checkInventory(self):
        if self.inventory: 
            for computer in self.inventory:
                print('{} ${}'.format(computer.description, computer.price))
            print("------------")
        else:
            print("No inventory to display.")

    def sell(self, computer):
        if computer in self.inventory: 
            self.inventory.remove(computer)
            print(computer.description, "sold!")
            del computer
        else:
            print("Item not found. Find another item to sell")

#All that's commented below worked at some point so I wanted to include it.
    # def buy(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
    #     computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
    #     self.itemID += 1
    #     computer.itemID = self.itemID
    #     self.inventory.append(computer)
     
    # def checkInventory(self):
    #     if self.inventory:
    #         for computer in self.inventory:
    #             print('Item ID: {}: {}. ${}.'.format(computer.itemID, computer.description, computer.price))
    #     else:
    #         print("No inventory to display.")


    # def sell(self, itemID):
    #     for computer in self.inventory:
    #         if computer.itemID == itemID:
    #             self.inventory.remove(computer)
    #             print("Item", computer.itemID,":", computer.description, "sold!")
    #         else: 
    #             print("Item", computer.itemID, ":", computer.description,  "not found. Please select another item to sell.")

    

def main():
     resaleshop = ResaleShop("Yaya's Tech")
     computer_1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

     resaleshop.buy(computer_1)
     resaleshop.checkInventory()

     computer_2 = Computer("Mac Pro (Late 2017)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

     resaleshop.buy(computer_2)

     resaleshop.checkInventory()

     resaleshop.sell(computer_2)

     computer_2.updatePrice(400)


    


if __name__ == "__main__": main()