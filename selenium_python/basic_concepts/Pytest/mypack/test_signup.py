import pytest

@pytest.fixture()
def setup():
    print("open the url to signup")
    yield
    print("close the browser after signout")

def test_signupbyEmail(setup):
    print("this is test Email signup")

def test_signupbyFacebook(setup):
    print("this is test Facebook signup")

# to run file we have to run it in terminal by typing 'pytest -v -s test_signup.py' or if we type only 'pytest -v -s' in terminal it will run all testcases inthe same module or 'pytest -v -s *full path to test folder* '
