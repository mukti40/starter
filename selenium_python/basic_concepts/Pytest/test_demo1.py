import pytest

def testMethord1():
    print("this is test methord 1")

def testMethord2():
    print("this is test methord 2")

# to run file we have to run it in terminal by typing 'pytest -v -s test_demo1.py' or if we type only 'pytest -v -s' in terminal it will run all testcases inthe same module  or 'pytest -v -s *full path to test folder* '  or 'pytest -v -s test_demo1.py::testMethord1' for running specific methord/testcase.