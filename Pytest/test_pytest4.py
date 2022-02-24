import pytest

@pytest.fixture()
def setup():
    print("This is setup")
    yield
    print("This is teardown")

def testMethod3(setup):
    print("This is method3")

def testMethod4(setup):
    print("This is method4")