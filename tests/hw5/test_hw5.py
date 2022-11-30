import unittest
import pandas as pd
from geopy.distance import distance
from pandas.util.testing import assert_frame_equal
from cruasan.hw5.hw5 import car_at_light
from cruasan.hw5.hw5 import safe_subtract
from cruasan.hw5.hw5 import retrieve_age_lbyl
from cruasan.hw5.hw5 import retrieve_age_eafp
from cruasan.hw5.hw5 import read_data
from cruasan.hw5.hw5 import count_simba
from cruasan.hw5.hw5 import get_day_month_year
from cruasan.hw5.hw5 import compute_distance
from cruasan.hw5.hw5 import sum_general_int_list


class Testsafe(unittest.TestCase):
    
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
    
    def test_retrieve_age_lbyl(self):
        example_dict = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
        example_dict2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
        self.assertEqual(retrieve_age_lbyl(example_dict), print(35))
        self.assertEqual(retrieve_age_lbyl(example_dict2),print("Some keys are missing"))

class Testsafe(unittest.TestCase):

    def test_retrieve_age_eafp(self):
        example_dict = {'name': 'Nard', 'last_name': 'Dog', 'birth': 1982}
        example_dict2 = {'name': 'Robert', 'last_name': 'California', 'gender': 'male'}
        self.assertEqual(retrieve_age_eafp(example_dict), print(40))
        self.assertEqual(retrieve_age_eafp(example_dict2), print("Some keys are missing"))

class Testsafe(unittest.TestCase):
    def test_read_data(self):
        file = "sample_diabetes_mellitus_data.csv"
        file2 = "dunder_mifflin_payroll.csv"
        output = read_data(file)
        expected_output = pd.read_csv(file)
        assert_frame_equal(output, expected_output)
        self.assertEqual(read_data(file2), print('There is no such file'))

class Testsafe(unittest.TestCase):
    def test_count_simba(self):
        example_list = ['Simba does not work here', 'Simba married Nala']
        expected_output = 2
        example_list2 = ['Timon & Pumba','Hakuna Matata']
        expected_output2 = 0
        self.assertEqual(count_simba(example_list), expected_output)
        self.assertEqual(count_simba(example_list2), expected_output2)

class Testsafe(unittest.TestCase):
    def test_get_day_month_year(self):
        example_df= get_day_month_year([datetime.date(2018,10,15), datetime.date(2019,10,15), datetime.date(2019,12,15)])
        test_d = {'day': [15, 15, 15], 'month': [10, 10, 12], 'year': [2018, 2019, 2019]}
        test_df = pd.DataFrame(data=test_d)
        assert_frame_equal(example_df,test_df)

class Testsafe(unittest.TestCase):
    def test_compute_distance(self):
        test_pair = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
        verify_pair = '[Distance(31.13186522205169), Distance(157.005827868894)]'
        self.assertEqual(str(compute_distance(test_pair)), verify_pair)

class Testsafe(unittest.TestCase):
        def test_sum_general_int_list(self):
            example_list1 = [[2], 3, [[1,2],5]]
            example_list2 = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
            expected_output1 = 13
            expected_output2 = 48
            self.assertEqual(sum_general_int_list(example_list1),expected_output1)
            self.assertEqual(sum_general_int_list(example_list2),expected_output2)