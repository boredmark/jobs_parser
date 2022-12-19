import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from pprint import pprint


class Parser:

	def __init__(self, url):
		self.url = url

	def get_response(self):
		ua = UserAgent()
		fake_ua = {'user-agent': ua.random}
		response = requests.get(url = self.url, headers=fake_ua)
		response.encoding = 'utf-8'
		return response

	def create_soup(self):
		response = self.get_response()
		soup = BeautifulSoup(response.text, 'html5lib')
		return soup

	def get_job_lins(self):
		soup = self.create_soup()
		links = soup.find_all('a','JobSearchCard-primary-heading-link')
		result = ['https://www.freelancer.com' + i['href'] for i in links]
		return result



