class Room(object):
    def __init__(self,room_name,room_type):
        self.room_name = room_name
        self.room_type = room_type
        #can either be office or LS
        
class Office(Room):
    def __init__(self,room_name):
        self.room_type = "office"
        self.maximum__number_of_occupants = 6
    
        
        
class LivingSpace(Room):
    def __init__(self,room_name):
        self.room_type = "living_space"
        self.maximum_number_of_occupants = 4
        
        
        
            