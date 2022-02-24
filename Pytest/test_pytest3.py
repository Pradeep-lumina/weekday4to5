import pytest

@pytest.fixture()
def setup():
    print("This is setup")
    yield
    print("This is teardown")

def testMethod1(setup):
    print("This is method1")

def testMethod2(setup):
    print("This is method2")