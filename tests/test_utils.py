import pytest
import unittest
import unittest.mock as um
from topological_sort import utils


def parse(data):
    with um.patch('builtins.open', um.mock_open(read_data = data)):
        with open("/file/to/path") as f:
            result = utils.load_data_from_file(f)
            return result

def test_parseinputdata():
    result = parse('1 2\n''3 4')
    assert result == {'1':['2'], '2': [], '3': ['4'], '4': []}

def test_emptystring():
    result = parse('')
    assert result == {}

def test_parseinputwithcycle():
    result = parse('1 2\n''2 1')
    assert result == {'1': ['2'], '2': ['1']}

def test_invalidinputdata():
    with pytest.raises(Exception):
        parse('1 2''\n3')