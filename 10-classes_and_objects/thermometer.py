import random
class Thermometer:

    def __init__(self):
        self.temperature = 0.0
        self.is_turned_on = False
    
    def __str__(self):
        msg = f"Temperature: {self.temperature}"
       
        if self.temperature >= 37.0:
            msg += "(Fever)"
        if self.temperature >= 41.0:
            msg += "\nCRITICAL TEMPERATURE!!"
        
        return msg

    def measure(self):
        if self.is_turned_on:
            self.temperature = random.randrange(340, 420) / 10
        else:
            print("")
            
    def turn_on(self):
        self.is_turned_on = True
    
    def turn_off(self):
        self.is_turned_on = False
        