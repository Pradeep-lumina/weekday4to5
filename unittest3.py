import unittest


class UnitMethod(unittest.TestCase):

    def test_firstmethod(self):
        print("First Method")

    def test_secondmethod(self):
        print("Second Method")

    def test_thirdmethod(self):
        print("Third Method")


if __name__ == "__main__":
    unittest.main()
