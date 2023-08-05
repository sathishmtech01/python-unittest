import unittest
from unittest.mock import Mock, patch
import mock_script.my_script

class TestMathOperations(unittest.TestCase):
	@patch('mock_script.my_script.add')
	def test_add(self,mock_add):
		# Create a Mock object
		mock_add = Mock()
		# Assign a return value to the mock function
		mock_add.return_value = 7
		
		# Use the mock function in place of the real 'add' function
		result = mock_script.my_script.add(3, 4)
		
		# Assertions
		self.assertEqual(result, 7)
		mock_add.assert_called_once_with(3, 4)
	@patch('mock_script.my_script.multiply')
	def test_multiply(self,mock_multiply):
		# Create a Mock object
		mock_multiply = Mock()
		# Assign a return value to the mock function
		mock_multiply.return_value = 12
		
		# Use the mock function in place of the real 'multiply' function
		result = mock_script.my_script.multiply(3, 4)
		
		# Assertions
		self.assertEqual(result, 12)
		mock_multiply.assert_called_once_with(3, 4)

if __name__ == '__main__':
	unittest.main()