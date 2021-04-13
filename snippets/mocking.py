import asyncio
import datetime
import pytest
from requests.exceptions import Timeout
import unittest
from unittest import TestCase
from unittest.mock import Mock




#
#  Testing async functions
#
class Sum:
    def sync_sum(self, x, y):
        return x+y

    async def async_sum(self, x, y):
        await asyncio.sleep(1)
        return x+y

@pytest.fixture()
def mock_sum(self, monkeypatch):
    future = asyncio.Future()
    monkeypatch.setattr(Sum, 'async_sum', future)
    return future

class TestAsync(TestCase):
    # Test ansync by waiting
    @pytest.mark.asyncio
    async def test_sum(self):
        # Arrange
        summer = Sum()
        #mock_sum.set_result(4)
        result = await summer.async_sum(1, 2)
        assert result == 3
 

    def test_sync_sum_no_mock(self):
        # Arrange
        summer = Sum()

        # Act
        res = summer.sync_sum(4, 8)

        # Assert
        self.assertEqual(12, res)

    def x_test_using_mock(monkeypatch):
        # Arrange
        monkeypatch.setattr(Sum, 'sync_sum', 42)
        summer = Sum()

        # Act
        result = summer.sync_sum( 4, 8)

        # Assert
        self.assertEqual(42, res)


@pytest.fixture
def input_value():
    input = 42
    return input

def test_multiple_of_3(input_value):
    assert input_value == 42



#
#  Parameterized tests
#
@pytest.mark.parametrize("x,y,expected", [
    (0, 0, 0),
    (0, 10, 10),
    (10, 0, 10),
    (10, 10, 20),
])
def test_sum_param(x, y, expected):
    # Arrange
    summer = Sum()

    # Act
    result = summer.sync_sum(x, y)

    # Assert
    assert result == expected



tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)
datetime = Mock()

def is_weekday():
    today = datetime.datetime.today()
    print(today)
    # Monday = 0, Sunday = 6
    return (0 <= today.weekday() < 5)

def get_future(days):
    today = datetime.datetime.tomorrow(days)
    return today

    
#
#  Mocks
#
class TestMocks(TestCase):
    def test_mock_sample(self):
        m = Mock()
        r = m.someFunc  # Creates on the fly
        f = m.doSomething("arg1")

        m.doSomething.assert_called()
        m.doSomething.assert_called_once()
        m.doSomething.assert_called_with("arg1")
        m.doSomething.assert_called_once_with("arg1")
        m.doSomething.call_count
        m.doSomething.call_args
        m.doSomething.call_args_list
        m.method_calls

    def test_mock_return(self):
        # Arrange

        # Act - Assert
        datetime.datetime.today.return_value = tuesday
        self.assertTrue(is_weekday())

        # Act - Assert
        datetime.datetime.today.return_value = saturday
        self.assertFalse(is_weekday())

    def test_sideeffects(self):
        datetime.datetime.tomorrow.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_future(10)


    def func_side_effect(self, day):
        print(f"Side effect of calling tomorrow with {day}")
        return 86

    def test_sideeffect_func(self):
        datetime.datetime.tomorrow.side_effect = self.func_side_effect
        res = get_future(10)
        self.assertEqual(86, res)

