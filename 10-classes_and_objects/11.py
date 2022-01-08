class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 0
        
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def show_status(self):
        on_text = "on" if self.is_on else "off"
        print(f"TV is {on_text}")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.turn_off()
tv.show_status()
