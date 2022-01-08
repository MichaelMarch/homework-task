class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 0
        self.channels = []
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def get_current_channel_name(self):
        return self.channels[self.channel_no] if self.channels[self.channel_no:] else ""

    def show_status(self):
        on_text = "on" if self.is_on else "off"
        current_channel_name = self.get_current_channel_name()
        print(f"TV is {on_text}, channel {self.channel_no}, ({current_channel_name})")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self, new_channels):
        self.channels = new_channels
    
    def show_channels(self):
        print(f"Available channels: {self.channels}")
    
tv = TV()
tv.turn_on()
tv.show_status()
tv.show_channels()
tv.set_channels(["Polsat", "TVN", "Filmbox",
                 "Discovery", "Animal Planet",
                 "Comedy Central", "FOX"])
tv.show_channels()
tv.show_status()
tv.set_channel(4)
tv.show_status()
tv.set_channel(2)
tv.show_status()
tv.set_channel(1)
tv.show_status()
tv.set_channel(6)






