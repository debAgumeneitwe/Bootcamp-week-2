import unittest
from room import Office, LivingSpace

class TestCase(unittest.TestCase):
    
    def test_office_room_type_is_correct(self):
        office = Office("blue office")
        self.assertEqual('office', office.room_type)
        
    
        
   