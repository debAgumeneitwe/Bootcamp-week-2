import unittest
from room import Office, LivingSpace

class TestCase(unittest.TestCase):
    
    def test_office_room_type_if_is_correct(self):
        office = Office("blue office")
        self.assertEqual("office", office.room_type)
        
    def test_space_type_if_is_living(self):
        living_space = LivingSpace("purple office")
        self.assertEqual("living_space", living_space.room_type)
        
        
    def test_maximum_occupants_in_livingspace(self):
        living_space = LivingSpace("purple office")
        self.assertEqual(4, living_space.maximum_number_of_occupants)
        
 
        
        
        
    
        
if __name__ == '__main__':
    unittest.main()
