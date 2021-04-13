import pytest
import asyncio


class Sum:
    def sync_sum(self, x, y):
        return x+y

    async def async_sum(self, x, y):
        await asyncio.sleep(1)
        return x+y


@pytest.fixture
def input_value():
    input = 42
    return input


@pytest.fixture()
def mock_sum(monkeypatch):
    future = asyncio.Future()
    monkeypatch.setattr(Sum, 'async_sum', future)
    return future


@pytest.mark.asyncio
async def test_sum():
    # Arrange
    summer = Sum()
    #mock_sum.set_result(4)
    result = await summer.async_sum(1, 2)
    assert result == 3


#
#  Makes use of fixture
#
def test_multiple_of_3(input_value):
    assert input_value == 42


#
# makes use of Mock
#
def test_using_mock(monkeypatch):
    # Arrange
    monkeypatch.setattr(Sum, 'sync_sum', 42)
    summer = Sum()

    # Act
    result = summer.sync_sum

    # Assert
    assert result == 42


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
