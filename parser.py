import requests
from fake_useragent import UserAgent



class Parser:

	def __init__(self, url):
		self.url = url


	def get_response(self):
		ua = UserAgent()
		fake_ua = {'user-agent': ua.random}
		response = requests.get(url = self.url, headers=fake_ua)
		return response


	def create_soup(self):
		pass