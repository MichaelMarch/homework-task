class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'    

    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)
    
    def set_name(self, name):
        self.name = name

uni = University()
uni.set_name("MIT")
uni.print_name()