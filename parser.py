import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv 


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

	def get_job_links(self):
		soup = self.create_soup()
		links = soup.find_all('a','JobSearchCard-primary-heading-link')
		result = ['https://www.freelancer.com' + i['href'] for i in links]
		return result

	def get_all_info(self):
		result = []
		links = self.get_job_links()
		for i in links[0:3]:
			try:
				ua = UserAgent()
				fake_ua = {'user-agent': ua.random}
				response = requests.get(url = i, headers=fake_ua)
				soup = BeautifulSoup(response.text, 'html5lib')
				title = soup.find('h1', 'PageProjectViewLogout-header-title').text
				price = soup.find('p','PageProjectViewLogout-header-byLine').text
				link = i
				result.append([title, price, link])
			except Exception as e:
				continue
		return result

	def create_csv(self):
		lst = ['title', 'price', 'link']
		with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
			writer = csv.writer(file, delimiter=';')
			writer.writerow(lst)

		for i in self.get_all_info():
			with open('res.csv', 'a', newline='', encoding='utf-8-sig') as file:
				writer = csv.writer(file, delimiter=';')
				writer.writerow(i)



