import unittest
from unittest.mock import Mock, patch
import processor

class TestProcessor(unittest.TestCase):
	
	@patch('data_service.fetch_data')
	def test_process_data(self, mock_fetch_data):
		# Create a custom mock for requests.Response
		mock_response = Mock()
		mock_response.json.return_value = [1, 2, 3]
		
		# Configure mock_fetch_data to return the custom mock response
		mock_fetch_data.return_value = mock_response
		print(processor.process_data())
		result = processor.process_data()
		
		self.assertEqual(result, 6)
		mock_fetch_data.assert_called_once()

if __name__ == '__main__':
	unittest.main()
