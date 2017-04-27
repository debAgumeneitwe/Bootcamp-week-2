class Person(object):
    def __init__(self,full_name,position):
        self.full_name = full_name
        self.position = position
        
        #while position == "Fellow" or position == "Staff"
        
        
        
class Fellow(Person):
    
    def __init__(self,full_name,living_option):
        #super(Fellow, self).__init__()
        self.position = "fellow"
        self.full_name = full_name
        self.living_option = living_option
        
        
        #creates room
        #has accomodation option
        
class Staff(Person):
    def __init__(self,full_name):
        self.position = "staff"
        self.full_name = full_name
        
        
        
        #can create office"""
        
    