import random

class CellPhone:
    
    def __init__(self, number, battery_life, songs):
        self.number = number
        self.battery_life = battery_life
        self.songs = songs
    
    def call(self, number):
        if self.battery_life <= 2:
            print("You can't call right now. Your phone is about to turn off!")
            return
        
        print(f"Calling {number}... as {self.number}")
        
        chance = random.choice([True, False])
        
        if chance:
            print("Connected. You can speak now")
        else:
            print("The call was rejected")
        
    def play_song(self):
        if self.battery_life <= 1:
            print("You can't play any songs right now. Your phone is about to turn off!")
            return
        song = random.choice(self.songs)
        print(f"Playing {song}")
    
    def __str__(self):
        return f"Number: {self.number}, Battery: {self.battery_life}, Songs: {self.songs}"
        
