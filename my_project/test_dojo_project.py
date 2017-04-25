import unittest
from dojo_room_allocation import Dojo

class Test_create_room(unittest.Testcase):
    def test_create_room_succcessfully(self):
        self.dojo = Dojo()
        initial_room_count = len(self.room.all_rooms)
        blue_office = self.create_room("Blue", "office")
        self.assertTrue(blue_office)
        new_room_count = len(self.all_rooms)
        self.assertEqual(new_room_count - initial_room_count,1)
        
        
        
    def test_create_room(self):
         yellow = Dojo('yellow', 'office')
        self.assertEqual(['yellow', 'office'],
                             [yellow.name, toyota.type_of_space],
                             msg='The room should have a name and type of space')
        
        
        
        
if __name__ == '__main__'
    unittest.main()
                                       
        
    