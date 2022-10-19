from unittest.mock import patch, MagicMock

import pytest

from tools import API, load_nums_from_file
from main import add, subtract, multiply, divide


class TestClass:

    @pytest.fixture()
    def numbers(self):
        x = 10
        y = 20
        z = 25
        return [x, y, z]

    def test_add_2(self, numbers):
        x = numbers[0]
        y = numbers[1]
        assert add(x, y) == 30

    @pytest.mark.custom_mark
    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (1.5, 0.5, 2), (10, 100, 110)])
    def test_add(self, x, y, z):
        assert add(x, y) == z

    @pytest.mark.custom_mark
    @pytest.mark.parametrize("x, y, z", [(2, 1, 1), (2, 1.5, 0.5), (110, 10, 100)])
    def test_subtract(self, x, y, z):
        assert subtract(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(0, 1, 0), (-1, 1, -1), (0.5, 10, 5)])
    def test_multiply(self, x, y, z):
        assert multiply(x, y) == z

    @pytest.mark.skip
    @pytest.mark.parametrize("x, y, z", [(0, 1, 0), (-1, 1, -1), (110, 100, 1.1)])
    def test_divide(self, x, y, z):
        assert divide(x, y) == z


class TestTools:
    def test_load_nums_from_file(self):
        test_data = ['1, 1', '1.5, 0.5', '10, 100']
        expected = [(1, 1), (1.5, 0.5), (10, 100)]

        fake_api = MagicMock()
        fake_api.get_data.return_value = test_data  # get_data method mocking
        with patch('tools.API', fake_api):
            # patch replaces the original object and context manager defines the scope of use of the mock
            result = load_nums_from_file()
            assert result == expected
