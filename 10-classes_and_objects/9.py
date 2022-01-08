class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'    
        self.full_name = "Cracow University of Economics"
    
    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)
        
    def set_name(self, name):
        self.name = name
    
    def print_full_name(self):
        print(self.full_name)
    
    def set_full_name(self, full_name):
        self.full_name = full_name

uni = University()
uni.print_name()
uni.print_full_name()
uni.set_name("MIT")
uni.set_full_name("Massachusetts Institute of Technology")
uni.print_name()
uni.print_full_name()