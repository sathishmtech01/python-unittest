import unittest
from unittest.mock import patch, Mock
import mock_script.math_op

class TestMathOperations(unittest.TestCase):
	
	@patch('mock_script.math_op.add', return_value=7)
	@patch('mock_script.math_op.multiply', return_value=12)
	@patch('mock_script.math_op.divide', return_value=2.0)
	def test_complex_operation(self, mock_divide, mock_multiply, mock_add):
		result = mock_script.math_op.complex_operation(3, 4)
		
		self.assertEqual(result, 14.0)
		mock_add.assert_called_once_with(3, 4)
		mock_multiply.assert_called_once_with(3, 4)
		mock_divide.assert_called_once_with(7, 12)
	
	def test_mock_objects(self):
		mock_add = Mock(return_value=10)
		mock_multiply = Mock(return_value=15)
		mock_divide = Mock(return_value=3.0)
		
		with patch('mock_script.math_op.add', mock_add), \
			patch('mock_script.math_op.multiply', mock_multiply), \
			patch('mock_script.math_op.divide', mock_divide):
			
			result = mock_script.math_op.complex_operation(5, 3)
		
		self.assertEqual(result, 45.0)
		mock_add.assert_called_once_with(5, 3)
		mock_multiply.assert_called_once_with(5, 3)
		mock_divide.assert_called_once_with(10, 15)

if __name__ == '__main__':
	unittest.main()
