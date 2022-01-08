class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 0
        self.channels = []
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def show_status(self):
        on_text = "on" if self.is_on else "off"
        print(f"TV is {on_text}")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self, new_channels):
        self.channels = new_channels
    
    def show_channels(self):
        print(self.channels)
    
tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
tv.show_channels()
tv.show_status()
tv.turn_off()


