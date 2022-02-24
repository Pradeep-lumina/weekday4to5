import unittest


def setUpModule():
    print("Setup module")

def tearDownModule():
    print("Tear Down Module")


class UnitMethod(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        print("Setup")

    @classmethod
    def tearDown(self) -> None:
        print("TearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print("Setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("TearDown Class")

    def test_firstmethod(self):
        print("First Method")

    def test_secondmethod(self):
        print("Second Method")

    def test_thirdmethod(self):
        print("Third Method")


if __name__ == "__main__":
    unittest.main()
