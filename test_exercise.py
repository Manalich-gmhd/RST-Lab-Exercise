import unittest
from exercise_class import RTSlab_exercise

class testFunctions(unittest.TestCase):
    """
     Class used to test the methods for class RTSlab_exercise 
     Author: Reynaldo Manalich
    """
    # creating the object used for test
    def setUp(self):
      self.exercise=RTSlab_exercise()
      
    
    def test_stringRotation(self):
      """
      testing method stringRotation
      """
      self.assertEqual(self.exercise.stringRotation("MyString", 2),'ngMyStri')
      self.assertEqual(self.exercise.stringRotation("MyString", 3),'ingMyStr')
      self.assertEqual(self.exercise.stringRotation("MyString", 4),'ringMySt')
      
    def test_aboveBelow(self):
      """
      testing method aboveBelow
      """
      self.assertEqual(self.exercise.aboveBelow([1, 5, 2, 1, 10],6),{'above': 1, 'below': 4})
      self.assertEqual(self.exercise.aboveBelow([8, 5, 1, 6, 2, 7, 9],4),{'above': 5, 'below': 2})
      self.assertEqual(self.exercise.aboveBelow([12, 23, 16, 34, 22, 41, 19],20),{'above': 4, 'below': 3})
      
    # destroying the object used for test
    def tearDown(self):
      del(self.exercise)
      
if __name__ == "__main__":
  unittest.main()       