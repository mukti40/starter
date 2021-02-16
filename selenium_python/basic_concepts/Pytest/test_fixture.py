import pytest

@pytest.fixture()
def setup():
    print("once before every methord")

def testMethord1(setup):
    print("this is test methord 1")

def testMethord2(setup):
    print("this is test methord 2")


# to run file we have to run it in terminal by typing 'pytest -v -s test_fixture.py' or if we type only 'pytest -v -s' in terminal it will run all testcases inthe same module.