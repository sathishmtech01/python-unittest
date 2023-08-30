# processor.py
import data_service

def process_data():
	data = data_service.fetch_data()
	print(data)
	result = sum(data)
	return result
