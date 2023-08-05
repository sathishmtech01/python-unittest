import unittest
from unittest.mock import patch
import mock_script.math_op

class TestMathOperations(unittest.TestCase):
	
	@patch('mock_script.math_op.add')
	@patch('mock_script.math_op.multiply')
	@patch('mock_script.math_op.divide')
	def test_complex_operation(self, mock_divide, mock_multiply, mock_add):
		mock_add.return_value = 7
		mock_multiply.return_value = 12
		mock_divide.return_value = 2.0
		
		result = mock_script.math_op.complex_operation(3, 4)
		
		self.assertEqual(result, 14.0)
		mock_add.assert_called_once_with(3, 4)
		mock_multiply.assert_called_once_with(3, 4)
		mock_divide.assert_called_once_with(7, 12)

if __name__ == '__main__':
	unittest.main()
