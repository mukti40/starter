import pytest

@pytest.fixture()
def setup():
    print("open the url to login")
    yield
    print("close the browser after logout")

def test_loginbyEmail(setup):
    print("this is test Email login")

def test_loginbyFacebook(setup):
    print("this is test Facebook login")

# to run file we have to run it in terminal by typing 'pytest -v -s test_login.py' or if we type only 'pytest -v -s' in terminal it will run all testcases inthe same module.
