#computer class/constructer
class Computer:

    #attributes of Computer Class
    description:str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    #initialize computer object with attributes
    def __init__(self, 
                 description, 
                 processor_type, 
                 hard_drive_capacity, 
                 computer_memory, 
                 operating_system, 
                 year_made, 
                 price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.computer_memory = computer_memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    #New price method, changes price attribute of new computer
    def update_price(self, new_price:int):
        self.price = new_price

    #Update operating system method, changes OS attribute of new computer
    def update_OS(self, new_OS:str):
        self.operating_system = new_OS