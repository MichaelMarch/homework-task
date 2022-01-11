class Statistics:
    
    def __init__(self):
        self.number_set = []

    def add_number(self):
        number = int(input("Enter a number: "))
        self.number_set.append(number)
    
    
    def find_max(self):
        result = max(self.number_set)
        print(f"The max value from {self.__str__()} is equal to: {result}")
    
    
    def find_min(self):
        result = min(self.number_set)
        print(f"The min value from {self.__str__()} is equal to: {result}")


    def arithmetic_mean(self):
        result = sum(self.number_set) / len(self.number_set)
        print(f"The arithmetic mean of {self.__str__()} is equal to: {result}")
    
    
    def median(self):
        sorted_set = sorted(self.number_set)
        l = len(sorted_set)
        
        if l & 1 == 0: #even 0 & 1 = 0
            result = (sorted_set[l // 2 - 1] + sorted_set[l // 2]) / 2
        else: #odd 1 & 1 = 1
            result = sorted_set[l // 2] 
        
        print(f"The median of {self.__str__()} is equal to: {result}")
        
    def __str__(self):
        return ", ".join(map(str, self.number_set))
        