import unittest
from dojo import Dojo
from person import Person, Fellow, Staff

class Test_create_room(unittest.TestCase):
    def test_create_room_succcessfully(self):
        self.dojo = Dojo()
        initial_room_count = len(self.dojo.all_rooms)
        blue_office = self.dojo.create_room("Blue", "office")
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count,1)
        

    def test_adds_staff_successfully(self):
        staff = Staff("John Bosco")
        self.assertEqual("staff", staff.position,
                        msg = "Added staff successfully")
        
        
    def test_adds_fellows_successfully(self):
        fellow = Fellow("John Bosco", "N")
        self.assertEqual("fellow", fellow.position,
                        msg = "Added staff successfully")
        

        
        
        
        
if __name__ == '__main__':
    unittest.main()
                     
   
        
        
 