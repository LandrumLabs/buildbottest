import unittest
import hovercraft

class TestHoverCraft(unittest.TestCase):
    def test_fullof(self):
        self.assertEqual(hovercraft.fullof(),"eels")

if __name__ == '__main__':
    unittest.main()
