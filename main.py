import parser

if __name__ == '__main__':
	link = 'https://www.freelancer.com/jobs/'
	parser = parser.Parser(link)
	parser.create_csv()
	print('Done!')