import unittest
from unittest.mock import patch
from equipment.framework.tests.BaseTest import BaseTest
from equipment.framework.helpers import print_if


class test_print_if(BaseTest):
    @patch('builtins.print')
    def test_true(self, mock_print):
        print_if(True, 'foo')
        mock_print.assert_called_with('foo')

    @patch('builtins.print')
    def test_false(self, mock_print):
        print_if(False, 'foo')
        mock_print.assert_not_called()


if __name__ == '__main__':
    unittest.main()
