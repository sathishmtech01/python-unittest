import unittest
from unittest.mock import Mock, MagicMock, patch
import mock_script.calculator

class Testcalculator(unittest.TestCase):
	
	def test_add(self):
		result = mock_script.calculator.add(3, 4)
		self.assertEqual(result, 7)
	
	def test_multiply(self):
		result = mock_script.calculator.multiply(3, 4)
		self.assertEqual(result, 12)
	
	def test_complex_operation(self):
		# Using MagicMock and Mock
		mock_add = MagicMock(return_value=7)
		mock_multiply = Mock(return_value=12)
		
		with patch('mock_script.calculator.add', mock_add), patch('mock_script.calculator.multiply', mock_multiply):
			result = mock_script.calculator.complex_operation(3, 4)
		
		self.assertEqual(result, 84)  # (7 + 12) * (7 * 12)

if __name__ == '__main__':
	unittest.main()
