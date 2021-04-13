import datetime
import pytest

import unittest
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch, create_autospec

from requests.exceptions import Timeout

from app2Test import get_holidays, fa
from app2Test import fb
from app2Test import C1

calls = []
def called_seq(seq):
    def called_in_seq(*args, **kwargs):
        calls.append(seq)
    return called_in_seq
#
#  Mocks
#
class TestMocksDecorator(TestCase):
    @patch('app2Test.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    def test_get_holidays_with_context_mgr(self):
        with patch('app2Test.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

    @patch('app2Test.f1')
    @patch('app2Test.f2')
    @patch('app2Test.f3')
    def test_fa_calls_correct_steps(self,
                            f3_patch: Mock,
                            f2_patch: Mock,
                            f1_patch: Mock):

        # Arrange
        f1_patch.side_effect = called_seq(1)
        f2_patch.side_effect = called_seq(2)
        f3_patch.side_effect = called_seq(3)

        # Act
        r = fa("X")

        # Assert
        f1_patch.assert_called_once()
        f2_patch.assert_called_once()
        f3_patch.assert_called_once()

        self.assertEqual(3, len(calls))
        self.assertEqual(1, calls[0])
        self.assertEqual(2, calls[1])
        self.assertEqual(3, calls[2])

    def test_patch_in_line(self):
        # print(fb("Y"))
        fb = Mock()
        print("Patch in-line after patch:" + str(fb("Y")))

    def test_patch_in_module(self):
        print("patch in module before patch:" + fb("Y"))
        # since we imported the function, it's now in this module
        with patch('mocking2.fb'):
            print("patch in module after patch:" + str(fb("Y")))
        print("patch in module after with:" + fb("Y"))

    def test_using_spec(self):
        mock_C1 = create_autospec(C1)
        print(mock_C1.a())
        print(mock_C1.b())
        with self.assertRaises(AttributeError):
            mock_C1.c()

    def test_C1_no_mock(self):
        res = C1().a_b()
        self.assertEqual("AB", res)

    @patch.multiple('app2Test.C1',
                   a=MagicMock(return_value='new_a'),
                   b=MagicMock(return_value='new_b'))
    def test_C1_multi_mock(self, **mocks):
        res = C1().a_b()
        self.assertEqual("new_anew_b", res)

