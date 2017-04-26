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
         yellow_office = Dojo('yellow', 'office')
        self.assertEqual(['yellow', 'office'],
                             [yellow.name, office.type_of_space],
                             msg='The room should have a name and type of space')
        
    def test_create_livingspace_room(self):
        green_living = Dojo('green', 'living')
        self.assertEqual(['green', 'living'],
                             [green.name, living.type_of_space],
                             msg='The room should have a name and type of space')
        
    def test_create_multiple_offices(self):
        
        self.assertListEqual([blue_office, black_office, brown_office],
                             [(blue, black, brown).name, living.type_of_space],
                             msg='Multiple offices can be created')
        
        
        
        
        
        
        
if __name__ == '__main__'
    unittest.main()
                                       
        
    