class Dojo(object):
    def __init__(self):
        
        self.all_rooms = []
        self.People = []
        self.initial_room_count = 0
        self.office_rooms = []
        self.living_rooms = []
        
        
        
    def create_room(self,room_name,room_type):
        
        new_room = Room(room_name,room_type)
        
                        
        if new_room.room_type == "office" or new_room.room_type == "living": 
            
            if new_room.room_type == "office":
                self.office_rooms.append(new_room)
                    
            elif new_room.room_type == "living":
                self.living_rooms.append(new_room)
               
        else:
            return ("Room type has to be either living or office")
        
        self.all_rooms = self.office_rooms + self.living_rooms
        
        
"""  
def add_person(self):
        accomodation option = N
        People.append(person)
        Raise ("Neil has been successfully added")
        
        if position == fellow and accomodation_option == N:
"""            
"""class Person(object):
    def __init__(self,name,position):
        self.full_name = full_name
        self.position = position
        
        while position == "Fellow" or position == "Staff"
        
        
        
class Fellow(Person):
    def __init__(self):
        self.position = fellow
        
        #creates room
        #has accomodation option
        
class Staff(Person):
    def __init__():
        pass
        #can create office"""
        
    
class Room(object):
    def __init__(self,room_name,room_type):
        self.room_name = room_name
        self.room_type = room_type
        #can either be office or LS
        
"""class Office(Room):
    def __init__():
        pass
        # maximum of 6
        
class Living_Space(Room):
    def __init__():
        pass
        #maximum of 4"""
        
            
        
           
    
        
       
        
