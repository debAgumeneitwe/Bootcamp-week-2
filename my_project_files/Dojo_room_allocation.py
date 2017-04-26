class Dojo(object):
    def __init__(self,room_name,room_type):
        self.room_name = room_name
        self.room_type = room_type
        self.all_rooms = []
        self.People = []
        self.initial_room_count = 0
        self.office_rooms = []
        self.living_rooms = []
        
        
        
    def create_room(self,room_name,room_type):
        new_room = Dojo(room_name,room_type)
        
        if room_type == "office" or room_type == "living": 
            
            if room_type == "office":
                self.office_rooms.append(new_room)
                    
            elif room_type == "living":
                self.living_rooms.append(new_room)
               
        else:
            return ("Room type has to be either living or office")
        
        self.all_rooms = self.office_rooms + self.living_rooms
           
    
        
       
        
