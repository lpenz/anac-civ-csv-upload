
import unittest
import anac

class TestBasic(unittest.TestCase):
    def test_import(self):
        try:
            anac.Anac()
        except:
            pass


