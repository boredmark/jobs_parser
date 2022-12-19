import sys
sys.path.append('/Users/valentyn/Documents/my_projects/jobs_parser')
import parser


def test_response_func():
	expect = 200
	p = parser.Parser('https://www.linkedin.com')
	assert p.get_response().status_code == expect

