import pytest

@pytest.fixture()
def setup():
    print("once before every methord")
    yield
    print("once after every methord")

def testMethord1(setup):
    print("this is test methord 1")

def testMethord2(setup):
    print("this is test methord 2")

# to run file we have to run it in terminal by typing 'pytest -v -s test_yield_fixture.py' or if we type only 'pytest -v -s' in terminal it will run all testcases inthe same module.

#
# to run file we have to run it in terminal by typing 'pytest -v -s test_yield_fixture.py' or if we type only 'pytest -v -s' in terminal it will run all testcases in the same module or we can give full path to run all the testcases "pytest -v -s D:\Users\Mukesh\Desktop\selenium_python\basic_concepts\Pytest"
