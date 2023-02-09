
"""computer.py: Creates a computer class and has update price and refurbish methods."""

__author__      = "Yaya Callahan"


from typing import Optional
class Computer:

    
    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    description: str 
    processor_type: str 
    hard_drive_capacity: int 
    memory: int 
    operating_system: str 
    year_made: int 
    price: int 

    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    
    def updatePrice(self, new_price):
        self.price = new_price


    def refurbish(self, new_os: Optional[str] = None):
        if self == None: 
            print("Not in inventory. Try again with a different item")
        else:
            if self.year_made < 2000:
                self.price = 0 # too old to sell, donation only
            elif self.year_made < 2012:
                self.price = 250 # heavily-discounted price on machines 10+ years old
            elif self.year_made < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self["price"] = 1000 # recent stuff
            




        

    # What methods will you need?