import sys
import pytest
from pytest_mock import mocker
from {{ cookiecutter.package_name }} import cli

@pytest.fixture
def response():
    return 'response-fixture'

def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert response == 'response-fixture'

def test_command_line_interface(mocker):
    """Test the CLI."""
    try:
        test_args = ['-h']
        mocker.patch('sys.argv', test_args)
        assert cli.main() == 0
    except Exception as e:
        mocker.stopall()
        raise(e)
