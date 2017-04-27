import unittest
from room import Office, LivingSpace

class TestCase(unittest.TestCase):
    
    def test_office_room_type_is_correct(self):
        office = Office("blue office")
        self.assertEqual("office", office.room_type, 
                         msg = "The room should be type office")
        
    def test_space_type_is_living(self):
        living_space = LivingSpace("purple office")
        self.assertEqual("living_space", living_space.room_type,
                         msg = "The room should be type of type living space")
        
        
    def test_maximum_occupants_in_livingspace(self):
        living_space = LivingSpace("purple office")
        self.assertEqual(4, living_space.maximum_number_of_occupants,
                         msg ="The maximum number of occupants is 4")
        
        
    def test_maximum_occupants_in_officespace(self):
        office_space = Office("black office")
        self.assertEqual(6, office_space.maximum_number_of_occupants,
                         msg = "The maximum number of occupants in office space is 6")
        
        
      
        
    def test_correct_room_name(self):
        #can not have characters
        
    def test_existence_of_room_name(self):    
 

        
        
    
        
if __name__ == '__main__':
    unittest.main()
