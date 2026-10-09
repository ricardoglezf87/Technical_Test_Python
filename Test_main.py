import unittest
from main import ReservatioManager 

class TestReservationManager(unittest.TestCase):
    def test_max_occupancy_ok(self):
        res = ReservatioManager.max_occupancy([(9, 12), (10, 13), (11, 14)])
        self.assertEqual(res,(3, 11, 12))
            
    def test_max_occupancy_ko(self):
        res = ReservatioManager.max_occupancy([(9, 12), (10, 13), (11, 14), (9, 12)])
        self.assertNotEqual(res,(3, 11, 12))
        
    def test_max_occupancy_empty(self):
        res = ReservatioManager.max_occupancy([])
        self.assertEqual(res,(0, None, None))
        
    def test_max_occupancy_same_max(self):
        res = ReservatioManager.max_occupancy([(9, 10), (10, 11), (11, 12)])
        self.assertEqual(res,(1, 9, 10))
            
    def test_max_occupancy_last_hour(self):
        res = ReservatioManager.max_occupancy([(21, 24), (23, 24), (19, 21)])
        self.assertEqual(res,(2, 23, 24)) 
        
    def test_max_occupancy_fist_hour(self):
        res = ReservatioManager.max_occupancy([(0, 3), (0, 1)])
        self.assertEqual(res,(2, 0, 1))         
        
    def test_max_multi_occupancy_ok(self):
        res = ReservatioManager.max_multi_occupancy([(9, 12), (10, 13), (11, 14)])
        self.assertEqual(res,(3, [(11, 12)]))
                
    def test_max_multi_occupancy_ko(self):
        res = ReservatioManager.max_multi_occupancy([(9, 12), (10, 13), (11, 14), (9, 12)])
        self.assertNotEqual(res,(3, [(11, 12)]))
        
    def test_max_multi_occupancy_empty(self):
        res = ReservatioManager.max_multi_occupancy([])
        self.assertEqual(res,(0, None))
        
    def test_max_multi_occupancy_same_max(self):
        res = ReservatioManager.max_multi_occupancy([(9, 10), (10, 11), (11, 12)])
        self.assertEqual(res,(1, [(9, 12)]))
        
    def test_max_multi_occupancy_same_max_multiple(self):
        res = ReservatioManager.max_multi_occupancy([(9, 10), (10, 11), (11, 12), (17,20),(20,21)])
        self.assertEqual(res,(1, [(9, 12),(17,21)]))
            
    def test_max_multi_occupancy_last_hour(self):
        res = ReservatioManager.max_multi_occupancy([(21, 24), (23, 24), (19, 21)])
        self.assertEqual(res,(2, [(23, 24)])) 
        
    def test_max_multi_occupancy_fist_hour(self):
        res = ReservatioManager.max_multi_occupancy([(0, 3), (0, 1)])
        self.assertEqual(res,(2, [(0, 1)]))     
                               
if __name__ == '__main__':
    unittest.main()

