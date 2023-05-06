import unittest

from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    '''
    Octoprime tires should be serviced only 
    when the sum of all values in the tire 
    wear array is greater than or equal to 3.
    '''
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.9, 0.9, 0.9]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.2, 0.3, 0.4]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())