import unittest

class UnitMethod(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        print("Setup")

    @classmethod
    def tearDown(self) -> None:
        print("TearDown")

    def test_firstmethod(self):
        print("First Method")

    def test_secondmethod(self):
        print("Second Method")

    def test_thirdmethod(self):
        print("Third Method")

if __name__ == "__main__":
    unittest.main()