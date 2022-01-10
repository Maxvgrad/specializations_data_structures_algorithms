from car_fueling import compute_min_refills
import unittest


class TestCarFueling(unittest.TestCase):

    def test_compute_min_refills(self):
        # self.assertEqual(2, compute_min_refills(950, 400, [200, 375, 550, 750]))
        self.assertEqual(-1, compute_min_refills(9500, 400, [200, 375, 550, 750]))

