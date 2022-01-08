class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'    

    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)

uni = University()
uni.print_name()