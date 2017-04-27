import unittest
from person import Fellow, Staff

class TestCase(unittest.TestCase):
    
    def test_correct_name_of_fellow(self):
        fellow = Fellow("paul Kasule","N")
        fellow.full_name = fellow.full_name.lower().replace(" ","")
        self.assertTrue(fellow.full_name.isalpha(),
                       msg= "name should not consist of special characters")

        
    def test_correct_name_of_staff(self):
        staff = Staff("John Bosco")
        staff.full_name = staff.full_name.lower().replace(" ","")
        self.assertTrue(staff.full_name.isalpha(),
                       msg = "name should consist of special characters")
        
        
        
    def test_if_person_is_fellow(self):
        fellow = Fellow("Paul Kasule", "N")
        self.assertEqual("fellow",fellow.position,
                        msg= "The position should be fellow")
        
        
    def test_if_person_is_staff(self):
        staff = Staff("John Bosco")
        self.assertEqual("staff",staff.position,
                        msg = "The position should be staff")
        
        
    #def test_living_option_of_fellow(self):
    
    #sdef test_gender_of_person(self):"""



if __name__ == '__main__':
    unittest.main()

        