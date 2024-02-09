class Computer:

    #construct computer object with attributes
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