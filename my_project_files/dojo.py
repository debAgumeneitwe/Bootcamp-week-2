from room import Room, Office, LivingSpace
from person import Person, Staff, Fellow

class Dojo(object):
    def __init__(self):
        self.all_rooms = {}
        self.People = []
        self.initial_room_count = 0
        self.office_rooms = []
        self.living_rooms = []
        self.new_room_count = self.initial_room_count + len(self.all_rooms)
        
        
        
    def create_room(self,room_name,room_type):
        new_room = Room(room_name,room_type,0)
                    
        #for room in self.all_rooms:
                    
        if new_room.room_name not in self.all_rooms.keys(): 
                #new_room = Room(room_name,room_type)

                if new_room.room_type == "office" or new_room.room_type == "living": 

                    if new_room.room_type == "office":
                        self.office_rooms.append(new_room)

                    elif new_room.room_type == "living":
                        self.living_rooms.append(new_room)

                else:
                    return ("Room type has to be either living or office")
                
        else:
            return("Please choose another name")

        self.all_rooms = self.office_rooms + self.living_rooms
        self.new_room_count ++ 1
        
        
"""       
    def add_person(self,full_name,position):
        person = Person
        accomodation option = N
        People.append(person)
        Raise ("Neil has been successfully added")
        
        if position == fellow and accomodation_option == N:            
"""

        
           
    
        
       
        