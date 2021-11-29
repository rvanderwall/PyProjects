import unittest
from parameterized import parameterized

class DD_Tests(unittest.TestCase):
    def setUp(self):
        pass

    @parameterized.expand([
        ("p1 v1", "p2 v1", "p1 v1 p2 v1"),
        ("p1 v2", "p2 v2", "p1 v2 p2 v2"),
    ])
    def test_can_get_values(self, p1, p2, expected):
        # Arrange

        # act
        res = f"{p1} {p2}"

        # Assert
        self.assertEqual(expected, res)

