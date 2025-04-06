# test_explore.py
import unittest
from lib.src.explore import cross_river

# # Generated in part by genAI
def create_test_raft(length, width):
    return {'length': length, 'width': width}

class TestRaftCrossing(unittest.TestCase):
    def test_valid_raft(self):
        raft = create_test_raft(5, 5)
        self.assertEqual(cross_river(raft), "Congratulations! You made it across the river!")

    def test_small_raft(self):
        raft = create_test_raft(1, 1)
        self.assertEqual(cross_river(raft), "Your raft is too small... you fell off!")

    def test_large_raft(self):
        raft = create_test_raft(15, 15)
        self.assertEqual(cross_river(raft), "Your raft is too big... it got stuck!")

    def test_low_volume_raft(self):
        raft = create_test_raft(3,3)
        self.assertEqual(cross_river(raft), "Your raft sank! Try again!")

    def test_float_values(self):
        raft = create_test_raft(3.5,7.3)
        self.assertEqual(cross_river(raft), "Congratulations! You made it across the river!")

    def test_float_and_int_values(self):
        raft = create_test_raft(3,7.3)
        self.assertEqual(cross_river(raft), "Congratulations! You made it across the river!")

    def test_negative_dimensions(self):
        raft = create_test_raft(-5, 5)
        self.assertEqual(cross_river(raft), "Please enter valid (nonzero) raft properties.")

    def test_zero_dimensions(self):
        raft = create_test_raft(0, 5)
        self.assertEqual(cross_river(raft), "Please enter valid (nonzero) raft properties.")

if __name__ == '__main__':
    unittest.main()

