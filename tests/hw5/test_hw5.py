import unittest
from cruasan.hw5.hw5 import car_at_light
from cruasan.hw5.hw5 import safe_subtract
from cruasan.hw5.hw5 import retrieve_age_lbyl


class Testcarlight(unittest.TestCase):
    
    def test_car_at_light(self):
        with self.assertRaises(Exception):
            car_at_light('blue')
        self.assertEqual(car_at_light('red'),str("stop"))

class Testsafe(unittest.TestCase):
    
    def test_safe_subtract(self):
        self.assertEqual(safe_subtract(5,2),3)
        self.assertEqual(safe_subtract(5.1,2.1),2.9999999999999996)
        self.assertEqual(safe_subtract('a',2),str("None"))

class Testsafe(unittest.TestCase):
    
    def test_safe_subtract(self):
        example_dict = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
        example_dict2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
        self.assertEqual(retrieve_age_lbyl(example_dict), print(35))
        self.assertEqual(retrieve_age_lbyl(example_dict2),print("Some keys are missing"))