# data_service.py
import requests

def fetch_data():
	response = requests.get('https://api.example.com/data')
	return response.json()
