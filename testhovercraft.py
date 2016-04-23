import unittest
import hovercraft

class TestHoverCraft(unittest.TestCase):
    def test_fullof(self):
        self.assertEqual(hovercraft.fullof(),"eels")
    def test_fullerof(self):
        self.assertEqual(hovercraft.fullof(),"fjord")

if __name__ == '__main__':
    unittest.main()
