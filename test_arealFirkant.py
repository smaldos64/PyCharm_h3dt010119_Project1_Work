from unittest import TestCase

import Main


class TestArealFirkant(TestCase):
    def test_arealFirkant(self):
        areal = Main.arealFirkant(8, 4)
        self.assertEqual(32, areal)
        #self.fail()

if __name__ == '__main__':
    TestCase()