import unittest
from unittest.mock import Mock, patch
import mock_script.my_script

class TestMathOperations(unittest.TestCase):
	
	def test_add(self):
		# Create a Mock object
		mock_add = Mock()
		# Assign a return value to the mock function
		mock_add.return_value = 7
		
		# Use the mock function in place of the real 'add' function
		with patch('mock_script.my_script.add', mock_add):
			result = mock_script.my_script.add(3, 4)
		
		# Assertions
		self.assertEqual(result, 7)
		mock_add.assert_called_once_with(3, 4)
	
	def test_multiply(self):
		# Create a Mock object
		mock_multiply = Mock()
		# Assign a return value to the mock function
		mock_multiply.return_value = 12
		
		# Use the mock function in place of the real 'multiply' function
		with patch('mock_script.my_script.multiply', mock_multiply):
			result = mock_script.my_script.multiply(3, 4)
		
		# Assertions
		self.assertEqual(result, 12)
		mock_multiply.assert_called_once_with(3, 4)

if __name__ == '__main__':
	unittest.main()